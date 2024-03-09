"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Olina Savčuková
email: olinkasavcuk@gmail.com
discord: savcukova
"""
import csv
import sys
import requests
from bs4 import BeautifulSoup


def get_html(odkaz):
    response = requests.get(odkaz)
    if response.status_code == 200:
        html = BeautifulSoup(response.text, "html.parser")
        return html
    else:
        print(f"Nepodařilo se získat HTML z {odkaz}.")
        return None


if len(sys.argv) == 3:
    html_obsah = get_html(sys.argv[1])
    output_file = sys.argv[2]
else:
    print("Nesprávný počet argumentů.")
    quit()


def towns() -> list:
    seznam_mest = []
    prvky_mest = html_obsah.find_all("td", "overflow_name")
    for mesto in prvky_mest:
        seznam_mest.append(mesto.text)
    return seznam_mest


def links() -> list:
    cesta = []
    link_elements = html_obsah.find_all("td", "cislo")
    for link in link_elements:
        town = link.find("a")
        if town:
            cesta.append(f"https://volby.cz/pls/ps2017nss/{town.get('href')}")
    return cesta


def id():
    id_town = []
    id = html_obsah.find_all("td", "cislo")
    for i in id:
        id_town.append(i.text)
    return id_town


def get_parties():
    parties = []
    link_town = links()
    htmls = requests.get(link_town[0])
    html = BeautifulSoup(htmls.text, "html.parser")
    one_party = html.find_all("td", "overflow_name")
    for party in one_party:
        parties.append(party.text)
    return parties


volici = []
ucast = []
platne_hlasy = []


def get_sum() -> None:
    cesta = links()
    for ces in cesta:
        html_cesta = requests.get(ces)
        html_ces = BeautifulSoup(html_cesta.text, "html.parser")
        
        voter = html_ces.find_all("td", headers="t2sa2")
        for volic in voter:
            volic = volic.text
            volici.append(volic.replace('\xa0', ' '))
        
        attend = html_ces.find_all("td", headers="t2sa3")
        for a in attend:
            a = a.text
            ucast.append(a.replace('\xa0', ' '))
        
        votes = html_ces.find_all("td", headers="t2sa6")
        for vote in votes:
            vote = vote.text
            platne_hlasy.append(vote.replace('\xa0', ' '))


def voters() -> list:
    all_links = links()
    hlasy = []
    for link in all_links:
        html = get_html(link)
        vote = html.find_all("td", "cislo", headers=["t1sb4", "t2sb4"])
        vote_percentages = []
        for percentage in vote:
            vote_percentages.append(percentage.text + " %")
        hlasy.append(vote_percentages)
    return hlasy


def create_rows() -> list:
    radky = []
    get_sum()
    mesta = towns()
    id_obci = id()
    hlasy = voters()
    
    zipped = zip(id_obci, mesta, volici, ucast, platne_hlasy)
    
    seznam = []
    for i, m, v, u, p in zipped:
        seznam.append([i, m, v, u, p])
    slouceni = zip(seznam, hlasy)
    for s, h in slouceni:
        radky.append(s + h)
    return radky


def main(odkaz, soubor):
    try:
        hlavicka = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy']
        obsah = create_rows()
        strany = get_parties()
        for strana in strany:
            hlavicka.append(strana)
        
        with open(soubor, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(hlavicka)
            writer.writerows(obsah)
    except IndexError:
        print("Nastala chyba.")
        quit()


if __name__ == "__main__":
    html_obsah = get_html(sys.argv[1])
    output_file = sys.argv[2]
    main(html_obsah, output_file)