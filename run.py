# this module is the driver of the program, calling a function in each module
from module_1.scrape_raw_data import scrape_raw_data
from module_2.purify_data import purify_web_data
from module_3.write_data_to_file import write_purified_data
import sys


url = sys.argv[1]
web_data_string = scrape_raw_data(url)  # web_data_string will be all the web data dumped as a string
cleaned_web_data = purify_web_data(web_data_string)  # this will roughly extract the comments, into a list
write_purified_data(cleaned_web_data)  # this purifies the list even more and writes each comment to file
