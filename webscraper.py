from bs4 import BeautifulSoup
import requests
import ast
import datetime as dt
import pandas as pd
import csv
import time 
import schedule

# suppress warning from urllib3
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# ------------ WEBSCRAPING -----------------------------------------------------------------------------------------------

# road temperatures
# https://rijkswaterstaatstrooit.nl/map-cache/timedContent/2021-12-28T23:25Z/road_temperatures.json

def scrape():
    url = 'https://rijkswaterstaatstrooit.nl/api/statistics'
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser') 
    statistics = ast.literal_eval(soup.text) # convert string to dict

    return statistics

def write_to_file(statistics):
    file = 'strooizout.csv'
    with open(file, 'a', newline='') as file:
        writer = csv.writer(file)
        # header = ['time'] + list(statistics.keys())
        # writer.writerow(header)
        now = dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        values = [now] + list(statistics.values())
        writer.writerow(values)

