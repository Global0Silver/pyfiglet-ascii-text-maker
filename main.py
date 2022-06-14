import pystyle
from pystyle import Colors, Colorate
import os
import time
import pyfiglet
from os import system
system("title " + "cool text gen")
clear = lambda: os.system('cls')
clear()

#the code is messy ik 

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
print ("leave blank for roman font")
fontus = input('Enter font:')
if(len(fontus) == 0):
  fontus = ('roman')
faded = input ("do u want the test to be faded?(y/n):")
clear()
#fade system
asciii = (pyfiglet.figlet_format(asci ,font = fontus ))
if faded == "n":
 print ("Colour list:")
 print(Colorate.Color(Colors.red, "Red", True))
 print(Colorate.Color(Colors.orange, "Orange", True))
 print(Colorate.Color(Colors.yellow, "yellow", True)) 
 print(Colorate.Color(Colors.green, "Green", True))
 print(Colorate.Color(Colors.blue, "blue", True))
 print(Colorate.Color(Colors.purple, "purple", True))
 print(Colorate.Color(Colors.pink, "pink", True))
 print ("leave blank if none")
 colour = input('Enter colour>')
 
if faded == "y":
 print ("Fade styles:")
 print(Colorate.Horizontal(Colors.blue_to_purple, "blue to purple  >1", 1))
 print(Colorate.Horizontal(Colors.blue_to_green, "blue to green   >2", 1))
 print(Colorate.Horizontal(Colors.red_to_purple, "red to purple   >3", 1))
 print(Colorate.Horizontal(Colors.yellow_to_red, "yellow to red   >4", 1))
 colour = ("ighdfhgf")

if faded == "y":
 fades = input (">")
 if fades == "1":
  fadecl = Colors.blue_to_purple
 elif fades == "2":
  fadecl = Colors.blue_to_green
 elif fades == "3":
  fadecl = Colors.red_to_purple
 elif fades == "4":
  fadecl = Colors.yellow_to_red
  
text = (pyfiglet.figlet_format(asci ,font = fontus ))

if faded == "y":
 print (Colorate.Vertical((fadecl), (asciii) , 1))
 
#the colour system(kinda sketch but hey if it works it works)
if colour == "Red" or colour == "red":
 print(Colors.red)
 
if colour == "Orange" or colour == "orange":
  print(Colors.orange)
   
if colour == "Yellow" or colour == "yellow":
  print(Colors.yellow)

if colour == "Green" or colour == "green":
  print(Colors.green)
  
if colour == "Blue" or colour == "blue":
  print(Colors.blue)
 
if colour == "Purple" or colour == "purple":
  print(Colors.purple)

if colour == "Pink" or colour == "pink":
  print(Colors.pink)

if faded == "n":
 print (pyfiglet.figlet_format(asci ,font = fontus ))
 print(Colors.white)
