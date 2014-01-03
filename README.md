gmail_arduino_notifier
======================

Sends a new mail alert serially to the arduino so you can control anything connected to the arduino. I used it to connect a walk/don't walk sign. 


- Will require the feedparser & pyserial modules 
- Store your serial port address

``` python
SERIALPORT = "/dev/cu.usbserial-A6008jDJ"
```
- Add your gmail login information 

``` python
d = feedparser.parse('https://username:password@mail.google.com/mail/feed/atom')
```


If you want to see how to connect physical things to the arduino you look at the full writeup here http://dtostillwell.com/?p=301

![alt tag](http://dtostillwell.com/wp-content/uploads/2010/04/4547666755_c2622571e5_b.jpg)
