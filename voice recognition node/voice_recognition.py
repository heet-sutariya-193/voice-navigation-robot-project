#!/usr/bin/env python3
import gi
import pocketsphinx
from pocketsphinx import LiveSpeech
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

Gst.init(None)

pipeline_description = 'autoaudiosrc ! audioconvert ! audioresample !  webrtcvad !pocketsphinx name=asr ! fakesink'

pipeline = Gst.parse_launch(pipeline_description)
asr = pipeline.get_by_name('asr')

hmm = "src/pocketsphinx/model/en-us/en-us"
lm = "src/pocketsphinx/model/en-us/custom.lm"
dict_path = "src/pocketsphinx/model/en-us/custom1.dict"
asr.set_property('lm', lm)
asr.set_property('dict', dict_path)
asr.set_property('hmm', hmm)

bus = pipeline.get_bus()
bus.add_signal_watch()
loop = GObject.MainLoop()

def fun(bus, message):
    if message.type == Gst.MessageType.ELEMENT:
        msg = message.get_structure()
        if msg and msg.get_name() == 'pocketsphinx':
            if msg['final']:
                print('voice recognized:', msg['hypothesis'])

bus.connect("message", fun)

pipeline.set_state(Gst.State.PLAYING)

try:
    loop.run()
except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
