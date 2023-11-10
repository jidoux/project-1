# What is this?
This is a python web scraping program, that takes a web page and creates three files in the Data folder, 
one with the raw unprocessed web data, one with the comments, and one with a 1-word sentiment analysis
of the comments using the OpenAI API.

# How to run it:
You must first download the files on github and put them into a specific folder.
Next, get your directory to be the directory you downloaded this repository in,
which is usually by the command ```cd <directory name>```
Then, create a conda environment with all the packages used in this program.
You can do this by doing the following command, just name it anything you want
```conda env create --file requirements.yml -n [ENTER NAME HERE]```
and then activate this environment with:
```conda activate [ENTER NAME HERE]```
Lastly, as long as your conda environment is activated, and you're in the directory
where you downloaded all the program's files, you are ready to run the program.
Enter in the following (run.py must be what you run to execute the program):
```python run.py <LINK>```

Important note: For reddit links to work, you will need to replace the www in the link with old,
everything else should be the same.
Also, you may have to put ?limit=<NUMBER> at the end of your URL, to get more comments
from the post.

