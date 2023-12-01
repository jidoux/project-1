# this module uses openai api to analyze the sentiment of each comment
# input: each comment
# output: the 1-word analysis of each comment
# the http status code 429 means rate limited, which is very relevant with this api
import hidden_api_key
import requests
import time

openai_api_key = hidden_api_key  # change this to your personal api key
endpoint = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {openai_api_key}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.0.0 Safari/537.36"
}


def get_sentiment(comment):
    try:
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"In one word is the following text Positive, Neutral, "
                                                     f"or Negative? : \"{comment}\""}]
        }
        response = requests.post(endpoint, headers=headers, json=data)
        num_iterations = 0
        while response.status_code == 429:
            print("currently being rate limited, pausing for 1 minute...")
            time.sleep(60)  # this basically waits until we stop being rate limited by the api
            response = requests.post(endpoint, headers=headers, json=data)
            num_iterations += 1
            if num_iterations > 8:  # so if it sleeps(waits) for 8 minutes I just save all the analysis and exit.
                # this happens a lot, but sleeping for a whole minute usually causes it work
                print("I believe you are being rate-limited by the OpenAI API. Please try again later.")
                return None
        if response.status_code == 200:
            result = response.json()
            sentiment = result['choices'][0]['message']['content']
            time.sleep(5)  # just to help with the rate limiting a bit
            return sentiment
    except Exception as e:
        print(f"Error occurred during sentiment analysis: {str(e)}")
        return None
