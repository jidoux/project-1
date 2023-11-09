# this module scrapes the raw data of a webpage
# input: a url
# output: returns all the raw web data, html included, and writes it to a file raw_site_data.txt
import requests
from bs4 import BeautifulSoup


def scrape_raw_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/100.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    my_file = open("CS325_p3/Data/raw/raw_site_data.txt", "w", encoding="utf-8")
    my_file.write(str(soup))  # so raw_site_data.txt has all the raw data of the webpage
    return soup
