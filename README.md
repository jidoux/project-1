# What is this?
This is a simple python web dumping program, all it does is dump the 
content—including html data of a website—into a file, called site_content.txt. This
file is only 1 line of the entire web page's content.

# How to run it:
You must first download the files on github and put them into a specific folder.
Next, get your directory to be the directory you downloaded this repository in,
which is usually by the command ```cd <directory name>```
Then, create a conda environment with all the packages used in this program.
You can do this by doing the following command, just name it anything you want
```conda create --name [ENTER NAME HERE] --file requirements.yaml```
and then activate this environment with:
```conda activate [ENTER NAME HERE]```
Lastly, as long as your conda environment is activated, and you're in the directory
where you downloaded all the program's files, you are ready to run the program.
Enter in the following:
```python main.py <LINK>```

Important note: For reddit links to work, you will need to replace the www in the link with old,
everything else should be the same.

