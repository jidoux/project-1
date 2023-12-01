# this module is the driver of the program, calling a function in each module
from CS_325p3.module_1.scrape_raw_data import scrape_raw_data
from CS_325p3.module_2.purify_data import purify_data
from CS_325p3.module_3.write_data_to_file import write_purified_data
from CS_325p3.module_5.generate_bar_graph import generate_bar_graph
import os


# Taking a given file path as input
url_path = input("What is the path to the url file: ")
url_file_name = input("What is the name of the url file: ")
# Define the input and output filenames
input_filename = url_path + "/" + url_file_name
current_directory = os.getcwd()
output_folder = current_directory + "\\CS_325p3\\Data"
raw_folder = os.path.join(output_folder, 'raw')
processed_folder = os.path.join(output_folder, 'processed')
directory_path = current_directory + "\\CS_325p3\\Data\\processed"
analyzed_folder = current_directory + "\\CS_325p3\\Data\\processed\\analyzed_site_data"

# Create the output directories if they don't exist
os.makedirs(raw_folder, exist_ok=True)
os.makedirs(processed_folder, exist_ok=True)

# Read the URLs from the input file
with open(input_filename, 'r') as file:
    urls = [line.strip() for line in file if line.strip()]

# Iterates through the URLs, naming each file based on the number of urls (I think)
for i, url in enumerate(urls):
    if url.strip():  # check if the line is not empty
        # Define the output filenames
        output_filename = f'raw_site_data_{i}.txt'
        comments_filename = f'processed_site_data_{i}.txt'

    # Call the scrape raw data function
    scrape_raw_data(url, os.path.join(raw_folder, output_filename))

    # Call the purify data function
    purify_data(os.path.join(raw_folder, output_filename), os.path.join(processed_folder, comments_filename))

for i, filename in enumerate(os.listdir(processed_folder)):
    if filename.endswith(".txt") and filename.startswith("processed_site_data_"):
        analyzed_filename = f'analyzed_site_data_{i}.txt'

        # Call the write_purified_data function
        write_purified_data(os.path.join(processed_folder, filename), os.path.join(analyzed_folder, analyzed_filename))

# this part deals with the creation of the bar graphs
analyzed_file_number = 1  # this is 1 due to the naming convention of the analyzed files, starting at 1
for i in range(5):  # this can definitely be improved, but it's a way to call the generate_bar_graph 5 times
    generate_bar_graph(output_folder, analyzed_file_number)
    analyzed_file_number += 1
