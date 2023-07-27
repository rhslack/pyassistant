import datetime

# code
def tellTime():
# This method will give the time
	time = str(datetime.datetime.now())
	# the time will be displayed like this "2020-06-05 17:50:14.582630"
	# nd then after slicing we can get time
	print(time)
	hour = time[11:13]
	min = time[14:16]
	return("Sono le " + hour + "Ore e" + min + "minution")	
"""
This method will take time and slice it "2020-06-05 17:50:14.582630" from 11 to 12 for hour
and 14-15 for min and then speak function will be called and then it will speak the current
time
"""
