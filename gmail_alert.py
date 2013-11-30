#Gmail notifier
 
#feedparser module download it from http://www.feedparser.org/
# pySerial module also needed
import serial, feedparser, time
 
# store your serial port address
SERIALPORT = "/dev/cu.usbserial-A6008jDJ"
 
#open serial port
ser = serial.Serial(SERIALPORT, 9600)
 
loop = 1
prevCheck = 0
 
while loop > 0:
	#set variable to hold parsed xml data
	d = feedparser.parse('https://username:password@mail.google.com/mail/feed/atom')
 
	#statement just to get title
	print d.feed.title
 
	newMail = len(d['entries'])
 
	#delay x seconds
	time.sleep(10)
 
	if newMail > 0:
    		#write to the serial port
       		ser.write('M')
       		print " you got mail"
	else: ser.write('N')