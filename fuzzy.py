import os
import colorama
from colorama import Back, Fore, Style
import requests
import sys

os.system("cls")
os.system("clear")
defwl = "wordlist.txt"

print(Fore.BLUE)
banner = """
--------------------------------
Web Site Directory & File Scanner And Admin Panel Finder
Coded by Xale ~ GitHub : @xaletr
--------------------------------
"""
print(banner)
print(Fore.YELLOW + Style.BRIGHT)
site = input("Site (Add http / https) >= ")
os.system("cls")
os.system("clear")

print(Fore.GREEN)

wordlist = input("Wordlist Directory >= ")
file = open(wordlist, "r")
lines = file.readlines()
for w in lines:
  try:
   r = requests.get(site + "/" + w)
   print(" ")
   print("URL : ", r.url, "                                      | Response Code : ", r.status_code)
  except:
   print("Bir Hata Olustu") 
