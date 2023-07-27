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
		print("Waining activating word...")
		if takeCommand.takeCommand().lower() == "jarvis":
			query = takeCommand.takeCommand().lower()
			if "ciao" in query:
				speaker.speak(hello.hello())
			
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
			elif "bye" in query:
				speaker.speak("Bye. Check Out GFG for more exciting things")
				exit()
			
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
			
			elif "tell me your name" in query:
				speaker.speak("I am Jarvis. L'assistente matto frollo")
			elif query != "none":
				speaker.speak(ask_question(query))
			else:
				speaker.speak("non ho capito")
