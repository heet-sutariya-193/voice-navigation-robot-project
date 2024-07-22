#!/usr/bin/env python3

import rospy
import gi
import pocketsphinx
from gi.repository import Gst, GObject
from std_msgs.msg import String

gi.require_version('Gst', '1.0')
Gst.init(None)

pipeline_description = 'autoaudiosrc ! audioconvert ! audioresample ! pocketsphinx name=asr ! fakesink'
pipeline = Gst.parse_launch(pipeline_description)
asr = pipeline.get_by_name('asr')

hmm = "src/pocketsphinx/model/en-us/en-us"
lm = "src/pocketsphinx/model/en-us/custom.lm"
dict_path = "src/pocketsphinx/model/en-us/custom1.dict"

asr.set_property('lm', lm)
asr.set_property('dict', dict_path)
asr.set_property('hmm', hmm)

pub = rospy.Publisher('voice_commands', String, queue_size=10)

bus = pipeline.get_bus()
bus.add_signal_watch()
loop = GObject.MainLoop()

def fun(bus, message):
    if message.type == Gst.MessageType.ELEMENT:
        msg = message.get_structure()
        if msg and msg.get_name() == 'pocketsphinx':
            if msg['final']:
                text = msg['hypothesis']
                rospy.loginfo('voice recognized:%s',text)
                pub.publish(text)

bus.connect("message",fun )


rospy.init_node('voice recognition node', anonymous=True)
pipeline.set_state(Gst.State.PLAYING)
    
try:
    loop.run()
except rospy.ROSInterruptException:
    pass
except KeyboardInterrupt:
    pass
    
pipeline.set_state(Gst.State.NULL)



