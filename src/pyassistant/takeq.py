from pyassistant.aigpt import ask_question
from pyassistant.speak import speak
from pyassistant.method import hello, takeCommand, tellTime
import wikipedia
import webbrowser

def Take_query():

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
		query = takeCommand.takeCommand().lower()
		if query != "none":
			speak(ask_question(query))

		# if "open geeksforgeeks" in query:
		# 	speak("Opening GeeksforGeeks ")
			
		# 	# in the open method we just to give the link
		# 	# of the website and it automatically open
		# 	# it in your default browser
		# 	webbrowser.open("www.geeksforgeeks.com")
		# 	continue
		
		# elif "open google" in query:
		# 	speak("Opening Google ")
		# 	webbrowser.open("www.google.com")
		# 	continue
			
		# elif "which day it is" in query:
		# 	# tellDay()
		# 	continue
		
		# elif "tell me the time" in query:
		# 	tellTime()
		# 	continue
		
		# # this will exit and terminate the program
		# elif "bye" in query:
		# 	speak("Bye. Check Out GFG for more exciting things")
		# 	exit()
		
		# elif "from wikipedia" in query:
			
		# 	# if any one wants to have a information
		# 	# from wikipedia
		# 	speak("Checking the wikipedia ")
		# 	query = query.replace("wikipedia", "")
			
		# 	# it will give the summary of 4 lines from
		# 	# wikipedia we can increase and decrease
		# 	# it also.
		# 	result = wikipedia.summary(query, sentences=4)
		# 	speak("According to wikipedia")
		# 	speak(result)
		
		# elif "tell me your name" in query:
		# 	speak("I am Jarvis. L'assistente matto frollo")
