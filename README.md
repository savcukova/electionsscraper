# ELECTIONS SCRAPER
Třetí projekt Engeto Akademie

#POPIS PROJEKTU
Projekt elections_scraper je nástroj napsaný v jazyce Python, který umožňuje automatické stahování informací o výsledcích voleb z webových stránek Českého statistického úřadu. Tento nástroj je užitečný pro politické analytiky, novináře a všechny ostatní, kteří potřebují získat a analyzovat data o výsledcích voleb.

## INSTALACE
1. Klonujte tento repozitář do svého lokálního prostředí.
2. Ujistěte se, že máte nainstalovaný Python a pip.
3. Nainstalujte potřebné závislosti pomocí příkazu:
   "pip install -r requirements.txt"

## POUŽITÍ
- Spusťte skript main.py s dvěma argumenty: URL adresou voleb a názvem výstupního souboru CSV
- Například:
python main.py "https://volby.cz/pls/ps2017nss/ps32xjazyk=CZ&xkraj=2&xnumnuts=2101" "benesov.csv"
- Skript stáhne data o výsledcích voleb z dané URL adresy a uloží je do zadaného výstupního souboru CSV
