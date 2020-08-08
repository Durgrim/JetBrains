import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style


#  Address new folder
dir_name = sys.argv[1]
#  Address path
path = os.getcwd()
try:
    #  New file on path/dir_name
    os.mkdir(f'{path}\\{dir_name}')
except FileExistsError:
    #  print('Error: File already exists')
    pass


def checker(url):
    # Basic checker (only detects dot presence on the URL address)
    if '.' in url:
        return True


def parse_html(text):
    text = BeautifulSoup(text, 'html.parser')
    parsed_text = ""
    for tag in text.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']):
        if tag.name == 'a':
            # Painting all links in blue color with Colorama
            parsed_text += Fore.BLUE + (tag.get_text() + "\n")
        else:
            parsed_text += Style.RESET_ALL + (tag.get_text() + "\n")
    return parsed_text


tabs_list = []
while True:
    inp = input()
    if inp == 'exit':
        break
    elif inp in tabs_list:
        with open(f'{path}\\{dir_name}\\{inp}.txt', "r") as n:
            print(n.read())
            tabs_list.append(inp)
    elif inp == 'back' and len(tabs_list) > 1:
        tabs_list.pop()
        back = tabs_list.pop()
        with open(f'{path}\\{dir_name}\\{back}.txt', "r") as n:
            print(n.read())
    else:
        if not checker(inp):
            print('error')
        else:
            if not inp.startswith("https://"):
                inp = "https://" + inp
            request = requests.get(inp)
            parsed = parse_html(request.text)
            print(parsed)
            tabs_list.append(inp[8:inp.find(".")])
            with open(f'{path}\\{dir_name}\\{inp[8:inp.find(".")]}.txt', "w") as n:
                n.write(parsed)
