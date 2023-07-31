from pyassistant.aigpt import ask_question
from pyassistant.speaker import Speaker
from pyassistant.method import hello, takeCommand, tellTime
import wikipedia
import webbrowser

def Take_query():
	# Initialize the Speaker
	speaker = Speaker()
	speaker.init()

	# calling the Hello function for
	# making it more interactive
	# hello.Hello()
	
	# This loop is infinite as it will take
	# our queries continuously until and unless
	# we do not say bye to exit or terminate
	# the program
	while(True):
		
		# taking the query and making it into
		# lower case so that most of the times
		# query matches and we get the perfect
		# output
		# print("Waining activating word...")
		# if takeCommand.takeCommand().lower() == "jarvis":
		query = takeCommand.takeCommand().lower()
		if "arrivederci" in query:
			speaker.speak("Bella, vado a dormire!")
			exit()
		elif "come stai" in query:
			print(hello.howareyou())
			speaker.speak(hello.howareyou())
		elif "sei il migliore" in query:
			print(hello.thebest())
			speaker.speak(hello.thebest())
		elif "apri google" in query:
			speaker.speak("Opening Google ")
			webbrowser.open("www.google.com")
			continue
			
		elif "which day it is" in query:
			# tellDay()
			continue
		
		elif "orario" in query:
			speaker.speak(tellTime.tellTime())
			continue
		
		# this will exit and terminate the program
		elif "ciao" in query:
			speaker.speak(hello.hello())
		
		elif "da wikipedia" in query:
			
			# if any one wants to have a information
			# from wikipedia
			speaker.speak("Checking the wikipedia ")
			query = query.replace("da wikipedia ", "")
			
			# it will give the summary of 4 lines from
			# wikipedia we can increase and decrease
			# it also.
			result = wikipedia.summary(query, sentences=4)
			speaker.speak("According to wikipedia")
			speaker.speak(result)
		
		elif "chi sei" in query:
			speaker.speak("Sono Jarvis. L'assistente del matto frollo")
		# elif "ai" in query:
		elif query != "none":
			speaker.speak(ask_question(query))
			# speaker.speak("non ho capito")
		else:
			pass
