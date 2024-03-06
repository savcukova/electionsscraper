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
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.prettify()

#najit tabulku s vysledky voleb
def find_table(soup):
    table = soup.find("table", {"class": "table"})
    if not table:
        print("Table not found.")
        return None
    else:
        return table 

def data_z_tabulky(table):
    all_rows = table.find_all("tr")[2:]
    data_election = []
    
    for row in all_rows:
        data = row.find_all("td")
        if len(data) >= 8:
            obec_data = {
                "kód obce": data[0].getText(),
                "název obce": data[1].getText(),
                "voliči v seznamu": data[2].getText(),
                "vydané obálky": data[3].getText(),
                "platné hlasy": data[4].getText(),
            }
        data_election.append(obec_data)