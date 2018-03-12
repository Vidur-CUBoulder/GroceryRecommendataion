#!usr/bin/python

from pygame import mixer
from gtts import gTTS
import os
import global_types

def text_op(speech):
	tts = gTTS(text=speech,lang='en-us',slow=False)
	tts.save("vocal.mp3")
	mixer.init()
	volval = mixer.Sound("./vocal.mp3")
	print("gtts_test: ",float((global_types.volume)/100))
	volval.set_volume(0.25)
	mixer.music.load('vocal.mp3')
	mixer.music.play()
	while mixer.music.get_busy() == True:
		continue
	mixer.stop()
	mixer.quit()
	os.remove("./vocal.mp3")
	

#if __name__ == '__main__':
#    text_op("Sameer Vaze")
