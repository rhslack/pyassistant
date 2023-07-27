import pyttsx4

def speak(audio):
	
	engine = pyttsx4.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and
	# [1]=female voice in set Property.
	# engine.setProperty('voice', voices[14].id)
	engine.setProperty('voice', "com.apple.ttsbundle.Alice-compact")
	
	# Method for the speaking of the assistant
	engine.say(audio)
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()
