# this module scrapes the raw data of a webpage, simple as that
# input: a url
# output: returns all the raw web data, html included, as a string, alongside
# output: writing that raw web data (as a string) to a file raw_site_data.txt
import urllib.request


def scrape_raw_data(url):
    web_data = urllib.request.urlopen(url)
    web_data_string = ""
    web_data_string += str(web_data.read())  # converts all the web page, html tags and all, into a string
    my_file = open("Data/raw/raw_site_data.txt", "w", encoding="utf-8")
    my_file.write(web_data_string)  # so raw_site_data.txt has all the raw data of the webpage
    return web_data_string
