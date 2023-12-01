# What is this?
This is a python web scraping program, that takes the URL of a Reddit Thread and scrapes its data into 3 Folders:
- Raw: Raw will contain all of the textual data to be found within the provided Reddit Thread
- Processed: Will contain only the comment data that will be further refined from the Raw folder
- Semantic Analysis: Will contain a 1-word semanitc descriptor of each comment after it has been passed through openAI API

# Prerequisites
  - Anaconda3
  - Git
  - openAi Account
  - openAi Key

# Obtaining an Account/Key
1. Open a browser and go to (https://openai.com)
2. Go to log in and sign up to create account you will need a valid accessible email and working phone number.
3. Fill in the requested information and then go to the email you provided to verify your new account and follow the steps prompted
4. Once logged in click on the tab called API reference located in the top left of the web page
5. Scroll down the page to the Authentication Header and click on the link which is Green highlighted and says "API Keys"
6. From here click the Create new Secret Key
   - A Very important note is to copy and paste the newly generated key to a location where it cannot be easily deleted, as this key is only generated once, if it is lost or deleted it cannot be retrieved.
7. Now you use the api key to generate api calls, in this program the api key goes in module_4 analyze_sentiment.py, under the variable openai_api_key
  
# Repository Installation
1. Begin with creating an envrionment  with all required libraries using the command ```conda env create --file requirements.yml -n [ENTER NAME HERE]```.
     * The "[Enter Name Hear]" portion being whatever you wand to name your environment. Example: conda env create --file requirements.yml -n PROJECT.
2. Activate your newely created environment using  ```conda Activate ``` folowed by the name of the env you just created.
3. From here you should use the command  ``` git pull https://github.com/jidoux/web-scraper.git``` to pull out all of the files contained within this repository to your local device
4. Once the repository has been pulled do ``` cd CS325_p3 ``` to get within the correct working directory.

# Running the Program 
1. Ensure you are in the correct directory of the program, with the right conda environment activated
2. To execute the program input ```python run.py```
3. Input the directory of the file with the input urls, and after that enter the file's name
4. Wait for the program to perform all the sentiment analysis
  
# NOTE:
- you must replace the "www" portion of your selected URL with "old" for example: [https](https://old.reddit.com)
- Also, you may have to put ?limit=<NUMBER> at the end of your URL, if all of the comments are not being scraped and tested.
- And also, you must replace the openai_api_key portion of the module_4 analyze_sentiment.py file with your own api key
