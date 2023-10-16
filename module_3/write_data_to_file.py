# this module iterates through a list of every comment and purifies each one
# individually, writing each one to a file as it goes
# input: each comment, as a list, with some html tags removed
# output: writes the completely purified web data to a file, 1 comment at a time
from module_2.purify_data import purify_comment


def write_purified_data(cleaned_web_data):
    num_iterations = 0
    my_file = open("Data/processed/processed_site_data.txt", "w", encoding="utf-8")
    for comment in cleaned_web_data:  # cleaned_web_data is a list, so each comment is separated
        if num_iterations > 2:  # reddit always has default comments at the start that this ignores
            comment = purify_comment(comment)  # calls purify_data.py functions to purify each comment individually
            my_file.write(comment + "\n")  # writing each comment to file separated by a newline
        num_iterations += 1
