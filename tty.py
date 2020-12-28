from sys import argv
from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()
try:
	version = argv[1]
except:
	version = "3"
sleep(3)
keyboard.type("python"+version+" -c 'import pty; pty.spawn(\"/bin/bash\")'")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(0.5)
keyboard.type("export TERM=xterm")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(0.5)
keyboard.press(Key.ctrl)
keyboard.press('z')
keyboard.release(Key.ctrl)
keyboard.release('z')
sleep(0.5)
keyboard.type("stty raw -echo; fg")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(0.5)
keyboard.press(Key.ctrl)
keyboard.press('c')
keyboard.release(Key.ctrl)
keyboard.release('c')
