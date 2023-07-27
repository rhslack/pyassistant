import pyttsx4
import threading

class Speaker():

	def __init__(self):
		self.engine = pyttsx4.init()
	
	def init(self):
		# getter method(gets the current value
		# of engine property)
		voices = self.engine.getProperty('voices')
		
		# setter method .[0]=male voice and
		# [1]=female voice in set Property.
		# self.engine.setProperty('voice', voices[14].id)
		self.engine.setProperty('voice', "com.apple.ttsbundle.Alice-compact")

		# # Start the speaker loop
		# self.engine.runAndWait()
	
	def speak(self, audio):
		thread = threading.Thread(target=self.say, args=(audio,))
		thread.start()
		# block until the new thread has terminated
		thread.join()


	def say(self, audio):
		# Method for the speaking of the assistant
		self.engine.say(audio)
		
		# Blocks while processing all the currently
		# queued commands
		self.engine.runAndWait()
