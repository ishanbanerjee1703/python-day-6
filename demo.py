'''
you need escape characters because lets say you print something, you need to add line breaks or things to separate things.

\n creates a new line
\t creates an indent or a tab

absolute vs relative paths: 
a path shows you where something is and from which folders, starting from home (usually users)

, everything is and how many layers in your item is. something like PWD is absolute, because it starts all the way from home

relative is if you do something like cd.., these depend on where you currently are and not overall


if you copy an absolute path then its not going to work on other devices because they probably dont exist on other devices. relative paths are more sturdy

modules and libraries
if you want the ability to create randomness, python doesn’t automatically have that so you need to import the concept of random. if in your project you need randomness, you would write
import random

then you get the ability to do some things with that
you could use random.randint(value1, value2) and it’l give you random value between these two numbers
random.choice selects a random option within whatever list you create

you can import math straight into python.


in order to have persistent data so data that stays when you stop program and start again, 



the following writes the sentence into demo.txt when you run demo.py
'''

with open("demo.txt", "w") as file: 
    file.write("File I/O is so fun!\n")
'''
if you add in \n then it basically will write that line only on a new line each time
'''
