import pyfiglet
import colorama
from colorama import Fore, Back, Style
colorama.init()




print ("""   ▄████  ██▓     ▒█████   ▄▄▄▄    ▄▄▄       ██▓         ██████  ██▓ ██▓  ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▓██▒    ▒██▒  ██▒▓█████▄ ▒████▄    ▓██▒       ▒██    ▒ ▓██▒▓██▒ ▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██░    ▒██░  ██▒▒██▒ ▄██▒██  ▀█▄  ▒██░       ░ ▓██▄   ▒██▒▒██░  ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓▒██░    ▒██   ██░▒██░█▀  ░██▄▄▄▄██ ▒██░         ▒   ██▒░██░▒██░   ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒░██████▒░ ████▓▒░░▓█  ▀█▓ ▓█   ▓██▒░██████▒   ▒██████▒▒░██░░██████▒▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒ ░ ▒░▓  ░░ ▒░▒░▒░ ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░▓  ░   ▒ ▒▓▒ ▒ ░░▓  ░ ▒░▓  ░░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░ ░ ░ ▒  ░  ░ ▒ ▒░ ▒░▒   ░   ▒   ▒▒ ░░ ░ ▒  ░   ░ ░▒  ░ ░ ▒ ░░ ░ ▒  ░░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░ ░   ░ ░ ░ ▒   ░    ░   ░   ▒     ░ ░      ░  ░  ░   ▒ ░  ░ ░     ░░     ░     ░░   ░ 
      ░     ░  ░    ░ ░   ░            ░  ░    ░  ░         ░   ░      ░  ░   ░     ░  ░   ░     
                               ░                                             ░                   
""")
x = input('Enter your text:')
fontus = input('Enter font:')
colour = input('Enter colour(red,green,blue):')

if colour == 'red':
   print (Fore.RED  )
   
if colour == 'green':
   print (Fore.GREEN)
   
if colour == 'blue':
   print (Fore.BLUE)   




print(pyfiglet.figlet_format(x,font = fontus))
