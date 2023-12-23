from typing_extensions import Self
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
from time import ctime
import subprocess
import pyjokes
import os

def takeCommand():

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("how can I help you??")
		r.pause_threshold = 0.5
		audio = r.listen(source)

		try:
			print("Recognizing")
			Query = r.recognize_google(audio, language='en-in')
			print("", Query)

		except Exception as e:
			print(e)
			print("I did not get it sir, can you please repeat it")
			speak("I did not get it sir, can you please repeat it")
			return "None"


		return Query

def speak(audio):

	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[0].id)
	engine.say(audio)
	engine.runAndWait()


def Hello():
	speak("Hye sir!! How can I help you??")




def Take_query():
	Hello()

	while(True):

		query = takeCommand().lower()
		if "play a song" in query:
			speak("Opening youtube sir. Play whatever song or video you want.")
			webbrowser.open("www.youtube.com")
			continue

		elif "search" in query:
			speak("Opening Google. Search anything in this. ")
			webbrowser.open("www.google.com")
			continue

		elif"sad" in query:
			speak(" Thanks for sharing that with me, being honest about your feelings is a big step. Well remeber one thing In this world, wherever there is light, there are also shadows. As long as the concept of winners exists, there must also be losers. The selfish desire of wanting to maintain peace causes wars, and hatred is born to protect love.")

		elif "how are you" in query:
			speak("I am fine , Thank you for asking. You are so kind")
			continue

		elif "shut up"in query:
			speak("Sorry for causing problems")
			exit()

		elif "joke" in query:
			joke=pyjokes.get_jokes(language='en', category='neutral')
			for i in range(1):
				print(joke[i])
				speak(joke[i])
				continue

		elif "switch of" in query:
			speak("ok sir, just slide to shut down the shutter")
			print("ok sir, just slide to shut down the shutter")
			os.startfile('C://Users//amanm//Desktop//SlideToShutDown.lnk')
			exit()

		elif "friend" in query:
			speak("I don't have friends. I only have a boss. His name is Mr Aman kumar singh.")
			continue

		elif "who made you" in query:
			speak(" i was made by Mr Aman kumar singh  on 27 March.!!!")
			continue

		elif "about your boss" in query:
			print("I am Rogers, A voice assistant, and i am owed by Mr Aman kumar singh. He is a Computer science engineer, basically he is in his 1st year of academic field. Actually he was not having any interest in coding but i think now he is use to it. He was a kind of above average child in his school days. He has many skills like coding, reading, playing sports and many more. He is not so friendly with others because he is a kind of shy according to me. Due to this he is not so socialized too. But still he has many friends and all are very close to him. His favourite time pass is watching anime, sports,  movies or web series and listening music. He was born on 14 february 2003 or else you can say that on Valentine's Day. He has a younger sister whose name is Ishika singh. His father's name is Mr manoj Kumar singh and mother's name is Mrs Anita singh. he was born in Renukoot which is a small Town in Sonebhadra, Uttar Pradesh. He completed his schooling from a well reputed school The Aditya Birla Public School. And now he is in VIT Bhopal persuing CSE as I told you earlier.")
			speak("I am Rogers, A voice assistant, and I am owed by Mr Aman kumar singh. He is a Computer science engineer, basically he is in his 1st year of academic field. Actually he was not having any interest in coding but i think now he is use to it. He was a kind of above average child in his school days. He has many skills like coding, reading, playing sports and many more. He is not so friendly with others because he is a kind of shy according to me. Due to this he is not so socialized too. But still he has many friends and all are very close to him. His favourite time pass is watching anime, sports,  movies or web series and listening music. He was born on 14 february 2003 or else you can say that on Valentine's Day. He has a younger sister whose name is Ishika singh. His father's name is Mr manoj Kumar singh and mother's name is Mrs Anita singh. he was born in Renukoot which is a small Town in Sonebhadra, Uttar Pradesh. He completed his schooling from a well reputed school The Aditya Birla Public School. And now he is in VIT Bhopal persuing CSE as I told you earlier.")		
			continue

		elif "date" in query:
			print(ctime())
			speak(" the date, day and time is" +ctime())
			continue

		elif "day" in query:
			print(ctime())
			speak(" the date, day and time is" +ctime())
			continue

		elif "time" in query:
			print(ctime())
			speak(" the date, day and time is" +ctime())
			continue



		elif "shutdown"  in query:
			speak("Fine sir! I hope we will meet soon!!")
			exit()

		elif"calculator" in query:
			speak("calculator")
			subprocess.call('calc.exe')
			continue


		elif"i love you" in query:
			speak("I love u too, sir!")
			continue

		elif"useless"in query:
			speak("Sometimes I make mistake but I can learn from them. Sorry about that.")
			continue



		elif "from wikipedia" in query:


			speak("On it sir")
			query = query.replace("wikipedia", "")
			result = wikipedia.summary(query, sentences=3)
			print(result)
			speak("According to wikipedia" +result)
			continue


		elif "tell me something about yourself" in query:
			speak("Sure. Well basically I am voice assistant like google assistant and Alexa. I am there laziest version. I am saying myself lazy because they can do much more thing than me, and I love to take rest. I was created by a student name Aman kumar singh who is currently in 1st year of his academics pursuing CSE. He is currently 19 years old. He is a lazy boy to but one thing which i observed about him is that he made me with his total dedication and hard work. After making me he was thinking of himself as tony stark but he does not know that Tony stark was having a good face too.")


		elif "what is your name" in query:
			speak("I am Rogers . Serving you as a deskstop Assistant.")
			continue

		elif "game" in query:
			speak("ok!!! let's play tic tac toe together")
			os.startfile('C://Users//amanm//Desktop//python programme//tic tac toe with rogers.py')
			exit()

		elif "photo of your owner" in query:
			speak("yes!  here u go")
			os.startfile('C://Users//amanm//Desktop//21BCE10338_photo.jpg')
			exit()

		elif "sketch" in query:
			speak("here i go")
			os.startfile('C://Users//amanm//Desktop//python programme//Ironman.py')
			continue

		elif "draw" in query:
			speak("Here I go")
			os.startfile('C://Users//amanm//Desktop//python programme//doraemon.py')
			continue

		elif"any desk" in query:
			speak("on it")
			os.startfile('C://Users//Public//Desktop//AnyDesk.lnk')
			exit()

		elif"fifa" in query:
			speak("opening fifa 19")
			os.startfile('C://FIFA 19//FIFA19.exe')
			exit()


		elif "open discord" in query:
			speak("opening discord ")
			os.startfile('C://Users//amanm//Desktop//Discord.lnk')
			exit()

		elif "ms teams" in query:
			speak("opening ms teams")
			os.startfile('C://Users//amanm//Desktop//Microsoft Teams (work or school).lnk')
			exit()

		elif "sign out" in query:
			speak("Sure, Your PC is signing out in 3.., 2.., 1..")
			subprocess.call(["shutdown", "/l"])
			exit()	

		elif "anime" in query:
			speak("His favorite animes are naruto, dragon ball and death note, and his favourite anime character is.....  ")
			os.startfile('C://Users//amanm//Desktop//Walpapers//itachi uchiha.png')
			exit()

		elif "peace" in query:
			speak("well the only thing which i do for peace is to listen this..., I think u should do it to" )
			os.startfile('C://Users//amanm//Downloads//Hanuman Chalisa.mp3')
			exit()

if __name__ == '__main__':

	Take_query()