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

#ZÍSKÁNÍ SEZNAMU MĚST V OKRESE - HOTOVO
def towns():
    list_towns = []
    town_elements = html_obsah.find_all("td", "overflow_name")
    for town in town_elements:
        list_towns.append(town.text)
    return list_towns

#ZÍSKÁNÍ ODKAZU PRO DALŠÍ DETAILY
def links():
    cesta = []
    link_elements = html_obsah.find_all("td", "cislo")
    for link in link_elements:
        town = link.find("a")
        if town:
            cesta.append("https://volby.cz/pls/ps2017nss/" + town.get("href"))
    return cesta

