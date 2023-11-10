# this module uses openai api to analyze the sentiment of each individual comment
# input: each comment, individually, and the list of comment analysis, solely to ensure the api is working rn
# output: the 1-word analysis of each comment
# the http status code 429 means rate limited, which is very relevant with this api
import hidden_api_key
import requests
import time
import sys


def analyze_comments(comment, list_of_comment_analysis):
    openai_api_key = hidden_api_key
    endpoint = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/100.0.0.0 Safari/537.36"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"what is the sentiment of the sentence, respond in only 1 word \"{comment}\""}],
    }
    response = requests.post(endpoint, headers=headers, json=data)
    # this line only happens if we are rate limited before anything else happens :/
    if len(list_of_comment_analysis) == 0 and response.status_code == 429:
        print("I believe you are being rate-limited by the OpenAI API. Please try again later.")
        my_file = open("CS325_p3/Data/processed/analyzed_site_data.txt", "w", encoding="utf-8")
        my_file.writelines(list_of_comment_analysis)
        my_file.close()
        sys.exit()
    if len(list_of_comment_analysis) != 0:  # to make sure that at least 1 api request has gone through
        num_iterations = 0
        while response.status_code == 429:
            print("currently being rate limited, pausing for 1 minute...")
            time.sleep(60)  # this basically waits until we stop being rate limited by the api
            response = requests.post(endpoint, headers=headers, json=data)
            num_iterations += 1
            if num_iterations > 8:  # so if it sleeps(waits) for 8 minutes I just save all the analysis and exit.
                # this happens a lot, but sleeping for a whole minute usually causes it work
                print("I believe you are being rate-limited by the OpenAI API. Please try again later.")
                my_file = open("CS325_p3/Data/processed/analyzed_site_data.txt", "w", encoding="utf-8")
                my_file.writelines(list_of_comment_analysis)
                my_file.close()
                sys.exit()
    if response.status_code == 200:
        result = response.json()
        sentiment = result['choices'][0]['message']['content']
        time.sleep(5)
        return sentiment
    else:  # This should only be reached if the status code is something that isn't 200 or 429.
        print(f"Invalid status code. Actual status code is {response.status_code}. Skipping...")
        return ""
