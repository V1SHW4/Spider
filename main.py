import socket

import os

import pyshorteners

import requests

os.system('clear')

print("""

░██████╗██████╗░██╗██████╗░███████╗██████╗░

██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗

╚█████╗░██████╔╝██║██║░░██║█████╗░░██████╔╝

░╚═══██╗██╔═══╝░██║██║░░██║██╔══╝░░██╔══██╗

██████╔╝██║░░░░░██║██████╔╝███████╗██║░░██║

╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝""")

print()

print("_____________________________")

print(" DEVELOPED BY LORD xRO ")

print("------------------------------")

print(" MEMBER OF TEAM CEO     ")

print("------------------------------")

print(" POWERED BY F SOCIETY   ")

print("______________________________")

print()

print()

url=input("Enter site url :>")

print()

print("IP ADDRESS  - ",socket.gethostbyname(url))

shortener=pyshorteners.Shortener()

x=shortener.tinyurl.short(url)

print("SHORT LINK  -"+"  "+x)

y=str(socket.gethostbyaddr(socket.gethostbyname(url)))

print("HOST        -"+"  "+y)

changed1="http://"+url

try:

	enc= requests.get(changed1)	print("ENCODED BY  -"+"  "+enc.encoding)

except:

	print("ENCODED BY  -"+"  "+"Failed")

cont=input("Enter [1]To Check Headers / [2]To Exit Tool")

if cont=="1":

	header= requests.get(changed1)

	vish=str(header.headers)

	print("HEADERS  -"+" "+vish)

elif cont=="2":

	print("TOOL EXITED")

else:

	print("SORRY,WRONG INPUT")
