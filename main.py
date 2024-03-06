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

#ziskani odkazu pro dalsi detaily
def get_links(html):
    links = []
    for link in html.select("td.cislo > a"):
        links.append("https://volby.cz/pls/ps2017nss/" + link.a["href"])
    return links

#ziskani informaci o volbach
def get_info(html):
    data = []
    for bunka in html.select("td[headers='sa2'], td[headers='sa3'], td[headers'sa6]"):
        data.append(bunka.text)
    return data