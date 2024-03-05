"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Olina Savčuková
email: olinkasavcuk@gmail.com@gmail.com
discord: savcukova
"""
import csv
import requests
from bs4 import BeautifulSoup

url = ""
output_file = ""

def election_results(url, output_file):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        table = soup.find("table", {"class": "table"})

        all_rows = table.find_all("tr")
        
        for row in all_rows:
            td = row.find_all("td")
            print(td) 
    

        
election_results("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103", "test")
            
    


