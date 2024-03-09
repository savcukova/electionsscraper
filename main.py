"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Olina Savčuková
email: olinkasavcuk@gmail.com@gmail.com
discord: savcukova
"""
import csv
import sys
import requests
from bs4 import BeautifulSoup

#ZÍSKÁNÍ DAT Z WEBOVÉ STRÁNKY - HOTOVO, FUNGUJE
def get_html(odkaz):
    response = requests.get(odkaz)
    if response.status_code == 200:
        html = BeautifulSoup(response.text, "html.parser")
        return html.prettify()
    else:
        print(f"Couldn't get HTML from {odkaz}.")
        return None

if len(sys.argv) == 3:
    html_obsah = get_html(sys.argv[1])
    output_file = sys.argv[2]
else:
    print("Nesprávný počet argumentů.")
    quit()

