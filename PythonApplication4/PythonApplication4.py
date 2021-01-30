import pyttsx3
from datetime import datetime
import winsound 
import sounddevice as sd 
from scipy.io.wavfile import write 
import wavio as wv

freq = 100
dur = 50

now = datetime.now()

current_hour = now.strftime("%H")
current_minute = now.strftime("%M")

engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#if it's before noon, or morning
if int(current_hour) <= 12:
    engine.say("Now is " + str(current_hour) + ' ' + str(current_minute) + 'AM')
    engine.say("Good morning, Quang!")
#if it's afternoon
elif int(current_hour) > 12 and int(current_hour) < 24:
    engine.say("Now is " + str(int(current_hour) - 12) + ' ' + str(current_minute) + 'PM')
    engine.say("Good afternoon, Quang!")
else:
    engine.say("Now is " + str(int(current_hour) - 12) + ' ' + str(current_minute) + 'PM')
    engine.say("Good night, Quang!")
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.say("I will record everything you say in these files after 5 'beeps' sound")
engine.save_to_file("The following files will recording whatever you say", 'test.mp3')
engine.runAndWait()
for i in range(0, 5):     
    winsound.Beep(freq, dur)     
    freq+= 100
    dur+= 50

  
# Sampling frequency 
freq = 44100
  
# Recording duration 
duration = 5
  
# Start recorder with the given values  
# of duration and sample frequency 
recording = sd.rec(int(duration * freq),  
                   samplerate=freq, channels=2) 
  
# Record audio for the given number of seconds 
sd.wait() 
  
# This will convert the NumPy array to an audio 
# file with the given sampling frequency 
write("recording0.wav", freq, recording) 
  
# Convert the NumPy array to audio file 
wv.write("recording1.wav", recording, freq, sampwidth=2)