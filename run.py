# this module is the driver of the program, calling a function in each module
from CS_325p3.module_1.scrape_raw_data import scrape_raw_data
from CS_325p3.module_2.purify_data import purify_data
from CS_325p3.module_3.write_data_to_file import write_purified_data
import sys
import os

# Define the input and output filenames

input_filename = "input.txt"
output_folder = "C:\\Users\\jdurl\\Reddit_Scraper\\web-scraper-main\\web-scraper-main\\CS_325p3\\Data"
raw_folder = os.path.join(output_folder, 'raw')
processed_folder = os.path.join(output_folder, 'processed')
directory_path = "C:\\Users\\jdurl\\Reddit_Scraper\\web-scraper-main\\web-scraper-main\\CS_325p3\\Data\\processed"
analyzed_folder = "C:\\Users\\jdurl\\Reddit_Scraper\\web-scraper-main\\web-scraper-main\\CS_325p3\\Data\\processed\\analyzed_site_data"

# Create the output directories if they don't exist
os.makedirs(raw_folder, exist_ok=True)
os.makedirs(processed_folder, exist_ok=True)

# Read the URLs from the input file
with open(input_filename, 'r') as file:
    urls = [line.strip() for line in file if line.strip()]

# Iterates through the URLs and scrape and filter comments for each URL
for i, url in enumerate(urls):
    if url.strip():  # check if the line is not empty
        # Define the output filenames
        output_filename = f'raw_site_data_{i}.txt'
        comments_filename = f'processed_site_data_{i}.txt'
       
       # Call the scrape_and_save function
    scrape_raw_data(url, os.path.join(raw_folder, output_filename))

        # Call the filter_and_save_comments function
    purify_data(os.path.join(raw_folder, output_filename), os.path.join(processed_folder, comments_filename))

for i, filename in enumerate(os.listdir(processed_folder)):
        if filename.endswith(".txt") and filename.startswith("processed_site_data_"):
            analyzed_filename = f'analyzed_site_data_{i}.txt'

            # Call the write_purified_data function
            write_purified_data(os.path.join(processed_folder, filename), os.path.join(analyzed_folder, analyzed_filename))

