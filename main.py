import urllib
import requests
import sys

web_data = urllib.request.urlopen(sys.argv[1])
my_file = open("site_content.txt", "w")
my_file.write(str(web_data.read()))