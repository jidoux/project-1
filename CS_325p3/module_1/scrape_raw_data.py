
import requests
from bs4 import BeautifulSoup


# Function to scrape and save data
def scrape_raw_data(url, output_filename):
    try:
        # Define a user agent to mimic a web browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'
        }

        # Sends a GET request to the provided URL with headers
        response = requests.get(url, headers=headers)

        # Checks if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Finds all text content within <p> and <h1> tags, modify as needed
            lines = [tag.text for tag in soup.find_all(['p', 'h1'])]

            # Combines the lines into a single string
            data = '\n'.join(lines)

            # Saves the data to the output file
            with open(output_filename, 'w', encoding='utf-8') as file:  
                file.write(data)

            print(f'Data scraped successfully and saved to {output_filename}')
        else:
            print(f'Error: Unable to fetch data from the URL. Status code: {response.status_code}')

    except Exception as e:
        print(f'An error occurred: {str(e)}')


