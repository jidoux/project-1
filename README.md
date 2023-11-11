# What is this?
This is a python web scraping program, that takes the URL of a Reddit Thread and scrapes its data into 3 Folders:
Raw: Raw will contain all of the textual data to be found within the provided Reddit Thread
Processed: Will contain only the comment data that will be further refined from the Raw folder
Semantic Analysis: Will contain a 1-word semanitc descriptor of each comment after it has been passed through openAI API

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
  
# Repository Installation
1. Begin with creating an envrionment  with all required libraries using the command ```conda env create --file requirements.yml -n [ENTER NAME HERE]```.
     * The "[Enter Name Hear]" portion being whatever you wand to name your environment. Example: conda env create --file requirements.yml -n PROJECT.
2. Activate your newely created environment using  ```conda Activate ``` folowed by the name of the env you just created.
3. From here you should use the command  ``` git pull https://github.com/jidoux/web-scraper.git``` too pull out all of the files contained within this repository to your local device
4. Once the repository has been pulled to the ``` cd CS325_p3 ``` to get within the correct working directory.

# Running the Program 

 To execute the program input ```python run.py [URL OF CHOICE] ```
   - The [URL OF CHOICE] should be replace with any url you intend on getting a semantic analysis performed on
  
# NOTE:
- you must replace the "www" portion of your selected URL with "old" for example: [https](https://old.reddit.com)
- Also, you may have to put ?limit=<NUMBER> at the end of your URL, if all of the comments are not being scraped and tested.

