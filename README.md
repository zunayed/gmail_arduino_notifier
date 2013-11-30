gmail_arduino_notifier
======================

Sends a new mail alert serially to the arduino so you can light and led/move a servo 


- Will require the feedparser & pyserial modules 
- Store your serial port address

``` python
SERIALPORT = "/dev/cu.usbserial-A6008jDJ"
```
- Add your gmail login information 

``` python
d = feedparser.parse('https://username:password@mail.google.com/mail/feed/atom')
```
