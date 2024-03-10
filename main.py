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

def town_id():
    #vraci list cisla obce
    id_town = []
    search_id = url_adress.find_all("td", "cislo")
    for t in search_id:
        id_town.append(t.text)
    return id_town

def town_name():
    #vraci list obci
    towns = []
    search_town = url_adress.find_all("td", "overflow_name")
    for t in search_town:
        towns.append(t.text)
    return towns

def town_link():
    #vrací url adresu k ziskani dalsich informaci o jednotlivych obcich
    link = []
    town_detail = url_adress.find_all("td", "cislo", "href")
    for t in town_detail:
        t = t.a["href"]
        link.append(f"https://volby.cz/pls/ps2017nss/{t}")
    return link

def get_parties():
    #vrací list stran ktere v dane obci kandiduji
    parties = []
    town = town_link()
    odkaz = requests.get(town[0])
    town_odkaz = BeautifulSoup(odkaz.text, "html.parser")
    party = town_odkaz.find_all("td", "overflow_name")
    for p in party:
        parties.append(p.text)
    return parties

def get_registered_voters():
    #vraci registrovane volice
    link = town_link()
    registered_voters = []
    for l in link:
        html_link = requests.get(l)
        obec = BeautifulSoup(html_link.text, "html.parser")
        registered = obec.find_all("td", headers="sa2")
        for r in registered:
            r = r.text
            registered_voters.append(r.replace('\xa0', ' '))
    return registered_voters

def get_participated_voters():
    #vrací celkovy pociet zucastnenych voliců
    link = town_link()
    participated_voters = []
    for l in link:
        html_link = requests.get(l)
        obec = BeautifulSoup(html_link.text, "html.parser")
        participated = obec.find_all("td", headers="sa3")
        for p in participated:
            p = p.text
            participated_voters.append(p.replace('\xa0', ' '))
    return participated_voters

def get_valid_votes():
    #vraci pocet platnych volicu
    link = town_link()
    valid_votes = []
    for l in link:
        html_link = requests.get(l)
        obec = BeautifulSoup(html_link.text, "html.parser")
        valid = obec.find_all("td", headers="sa6")
        for v in valid:
            v = v.text
            valid_votes.append(v.replace('\xa0', ' '))
    return valid_votes

def get_party_votes():
    #vraci list, kde pise kolik hlasu ziskala dana strana
    link = town_link()
    votes = []
    for l in link:
        vote_list = []
        obec = get_html(l)
        vote = obec.find_all("td", "cislo", headers=["t1sb3", "t2sb3"])
        for v in vote:
            vote_list.append(v.text)
        votes.append(vote_list)
    return votes

def create_data():
    slouceni = []
    id = town_id()
    town = town_name()
    registered_voter = get_registered_voters()
    participated_voter = get_participated_voters()
    valid_voter = get_valid_votes()
    sum_votes = get_party_votes()
    
    zipped = zip(id, town, registered_voter, participated_voter, valid_voter)
    temp_list = []
    for i, t, r, p, v in zipped:
        temp_list.append([i, t, r, p, v])
    
    zip2 = zip(temp_list, sum_votes)
    for t, s in zip2:
        slouceni.append(t + s)
    return slouceni

def main(odkaz, soubor):
    headers = ['Číslo obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy']
    main_data = create_data()
    parties = get_parties()
    for p in parties:
        headers.append(p)
    
    with open(soubor, "w", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(main_data)

if __name__ == "__main__" and len(sys.argv) == 3:
    url_adress = get_html(sys.argv[1])
    output_file = sys.argv[2]
    main(url_adress, output_file)
else:
    print("Špatný počet argumentů")
    quit()