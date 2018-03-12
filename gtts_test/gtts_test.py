#!usr/bin/python

from pygame import mixer
from gtts import gTTS

tts = gTTS(text='You picked up milk and eggs, you might also like to purchase flour',lang='en-uk',slow=False)
tts.save("hello.mp3")
mixer.init()
mixer.music.load('hello.mp3')
mixer.music.play()

while mixer.music.get_busy() == True:
    continue
