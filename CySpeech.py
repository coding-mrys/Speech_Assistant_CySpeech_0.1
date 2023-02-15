import speech_recognition as sr
import webbrowser
from gtts import gTTS
from playsound import playsound
import os
from time import ctime
import random
import pyjokes
import time
from urllib import request
from bs4 import BeautifulSoup
import requests

speech_engine = sr.Recognizer()
language="en"
t=7
txt=""

def speech():

    with sr.Microphone() as micro:
        tts = gTTS(text="How can i help you?",
        lang=language,slow=False)
        tts.save("audio.mp3");playsound("audio.mp3")
        os.remove("audio.mp3")

        #start recording
        print("recording...")
        audio = speech_engine.record(micro, duration=t)
        print("recognition...")
        txt = speech_engine.recognize_google(audio, language="en-EN")
        print(txt)

        #start recognition
        words = txt.split()
        if words[0] == "open":
            txt="OK, opening"+words[1]

            tts = gTTS(text=txt,
            lang=language,slow=False)
            tts.save("audio.mp3");playsound("audio.mp3")
            os.remove("audio.mp3")

            webbrowser.open("www."+words[1])

        elif words[0] == "time":
            txt="Ok, It's: "+str(ctime())

            tts = gTTS(text=txt,
            lang=language,slow=False)
            tts.save("audio.mp3");playsound("audio.mp3")
            os.remove("audio.mp3")

        elif words[0] == "calculate":
            
            if words[2] == "+":
                result = int(words[1]) + int(words[3]) 
                txt = str(words[1]) + " plus " + str(words[3]) + " is " + str(result)

            elif words[2] == "-":
                result = int(words[1]) + int(words[3]) 
                txt = str(words[1]) + " minus " + str(words[3]) + " is " + str(result)

            elif words[2] == "x":
                result = int(words[1]) * int(words[3]) 
                txt = str(words[1]) + " times " + str(words[3]) + " is " + str(result)

            elif words[2] == "/" or words[2] == "through":
                result = int(words[1]) / int(words[3]) 
                txt = str(words[1]) + " through " + str(words[3]) + " is " + str(result)

            tts = gTTS(text=txt,
            lang=language,slow=False)
            tts.save("audio.mp3");playsound("audio.mp3")
            os.remove("audio.mp3")

        elif words[0] == "joke" or words[0] == "jokes":
            jokes = pyjokes.get_jokes(language="de", category="twister")
            txt = random.choice(jokes)

            tts = gTTS(text=txt,
            lang=language,slow=False)
            tts.save("audio.mp3");playsound("audio.mp3")
            os.remove("audio.mp3")

        #get result from google
        elif words[0] == "search":
            end=""
            url = f"https://en.wikipedia.org/wiki/"+words[1]
            page  = requests.get(url)
            soup = BeautifulSoup(page.content,"html.parser")
            box = soup.find("div",attrs={"class":"mw-parser-output"})
            rows = box.find_all("p")

            output1 = rows[0].text.split()
            output2 = rows[1].text.split()

            output = output1+output2

            length = len(output)

            for x in range(length):
                end+=output[x]+" "

            print(end)
            txt=end
                        
            tts = gTTS(text=txt,
            lang=language,slow=False)
            tts.save("audio.mp3");playsound("audio.mp3")
            os.remove("audio.mp3")

        elif words[0] == "name":
            file = open("namelist.txt","r")
            name = file.read()
            txt="Hello, " + name

            tts = gTTS(text=txt,
            lang=language,slow=False)
            tts.save("audio.mp3");playsound("audio.mp3")
            os.remove("audio.mp3")
        
        elif words[0] == "rename":
            file = open("namelist.txt","w")
            file.write(words[1])
            txt = "Ok, your name is now " + words[1]

            tts = gTTS(text=txt,
            lang=language,slow=False)
            tts.save("audio.mp3");playsound("audio.mp3")
            os.remove("audio.mp3") 

        elif words[0] =="timer":
            x=0
            txt = "Ok, set timer to " + words[1] + words[2]

            tts = gTTS(text=txt,
            lang=language,slow=False)
            tts.save("audio.mp3");playsound("audio.mp3")
            os.remove("audio.mp3") 
            
            x+=1
            if x>0 and words[2] == "seconds":
                time.sleep(int(words[1]))

            elif x>0 and words[2] == "minutes":
                time.sleep(int(words[1])*60)

            txt="Ok, "+words[1]+words[2]+ "done!"
            tts = gTTS(text=txt,
            lang=language,slow=False)
            tts.save("audio.mp3");playsound("audio.mp3")
            os.remove("audio.mp3") 

        elif words[0] == "YouTube":
            title=""
            for x in range(len(words)-1):
                title+=words[x+1] + " "
            
            txt="Ok, searching on YouTube for "+title
            tts = gTTS(text=txt,
            lang=language,slow=False)
            tts.save("audio.mp3");playsound("audio.mp3")
            os.remove("audio.mp3") 

            webbrowser.open("https://www.youtube.com/results?search_query="+title)

        #no function found...
        else:
            txt="Sorry, I didn't understand that"

            tts = gTTS(text=txt,
            lang=language,slow=False)
            tts.save("audio.mp3");playsound("audio.mp3")
            os.remove("audio.mp3")



#|''\    /''|  |'''''''\  |'''   |'''|  |''''''''|
#|   \  /   |  |   []  |  |  |__|   |  |    _____|
#|    \/    |  |      /   \        /   \____   \
#|          |  |  |\  \    ''''|  |        \    \
#|   |\/\   |  |  | \  \    __|  |    |''''    /
#|__|   |___|  |__|  \__\  |_____|   |________/ by mrys.exe©


