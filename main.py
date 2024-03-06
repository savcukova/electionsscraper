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

url = ""
output_file = ""

#ziskani dat z webove stranky
def election_results(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Couldn't load website.")
        return None
    elif response.status_code == 200:
        html = BeautifulSoup(response.text, "html.parser")
        return html.prettify()


#ziskani mest
def towns(html):
    towns = []
    elementy_obci = html.select("td.overflow_name")
    for town in elementy_obci:
        towns.append(town.text)
    return towns