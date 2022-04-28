#!/usr/bin/env python
import pystyle
from pystyle import Colors, Colorate
import os
import time
import pyfiglet
from os import system
system("title " + "cool text gen")



intro =  """
  ▄████  ██▓     ▒█████   ▄▄▄▄    ▄▄▄       ██▓         ██████  ██▓ ██▓  ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▓██▒    ▒██▒  ██▒▓█████▄ ▒████▄    ▓██▒       ▒██    ▒ ▓██▒▓██▒ ▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██░    ▒██░  ██▒▒██▒ ▄██▒██  ▀█▄  ▒██░       ░ ▓██▄   ▒██▒▒██░  ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓▒██░    ▒██   ██░▒██░█▀  ░██▄▄▄▄██ ▒██░         ▒   ██▒░██░▒██░   ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒░██████▒░ ████▓▒░░▓█  ▀█▓ ▓█   ▓██▒░██████▒   ▒██████▒▒░██░░██████▒▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒ ░ ▒░▓  ░░ ▒░▒░▒░ ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░▓  ░   ▒ ▒▓▒ ▒ ░░▓  ░ ▒░▓  ░░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░ ░ ░ ▒  ░  ░ ▒ ▒░ ▒░▒   ░   ▒   ▒▒ ░░ ░ ▒  ░   ░ ░▒  ░ ░ ▒ ░░ ░ ▒  ░░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░ ░   ░ ░ ░ ▒   ░    ░   ░   ▒     ░ ░      ░  ░  ░   ▒ ░  ░ ░     ░░     ░     ░░   ░ 
      ░     ░  ░    ░ ░   ░            ░  ░    ░  ░         ░   ░      ░  ░   ░     ░  ░   ░     
                               ░                                             ░                   
"""
print(Colorate.Vertical(Colors.blue_to_purple, intro, 1))
print(Colors.white)
asci = input('Enter your text:')
fontus = input('Enter font:')

print ("Colour list:")
print(Colorate.Color(Colors.red, "Red", True))
print(Colorate.Color(Colors.orange, "Orange", True))
print(Colorate.Color(Colors.yellow, "yellow", True)) 
print(Colorate.Color(Colors.green, "Green", True))
print(Colorate.Color(Colors.blue, "blue", True))
print(Colorate.Color(Colors.purple, "purple", True))
print(Colorate.Color(Colors.pink, "pink", True))
print ("leave blank if none")
colour = input('Enter colour:')

if colour == "Red" or colour == "red":
 print(Colors.red)
 if colour == "Orange" or colour == "orange":
  print(Colors.orange)
 elif colour == "Yellow" or colour == "yellow":
  print(Colors.yellow)
 elif colour == "Green" or colour == "green":
  print(Colors.green)
 elif colour == "Blue" or colour == "blue":
  print(Colors.blue)
 elif colour == "Purple" or colour == "purple":
  print(Colors.purple)
 elif colour == "Pink" or colour == "pink":
  print(Colors.pink)
#else:
 # print(Colorate.Error(Colors.red, "that colour doesnt exist check the capitalization", True)) #fix this
  #print ("Restarting...")
  #time.sleep(1)
  #os.system("python w.py")
  

if(len(fontus) == 0):
  fontus = ('roman')

text =print (pyfiglet.figlet_format(asci ,font = fontus ))
print(Colors.white)

input ("")
