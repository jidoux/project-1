# this module uses openai api to analyze the sentiment of each individual comment
# input: each comment, individually, and the list of comment analysis, solely to ensure the api is working rn
# output: the 1-word analysis of each comment
# the http status code 429 means rate limited, which is very relevant with this api
#import hidden_api_key
import requests
import openai
import time
import sys
import os

openai.api_key = "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"

def get_sentiment(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages =[{"role":"user","content": f"In one word is the following text Positive, Neutral, or Negative? : \n{text}\n"}],
            max_tokens=1,
        )
        sentiment = response['choices'][0]['message']['content']
        return sentiment
    except Exception as e:
        print(f"Error occurred during sentiment analysis: {str(e)}")
        return None


