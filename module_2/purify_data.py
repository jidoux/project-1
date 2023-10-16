# this module deals with all purification of the raw website data
# it just does a lot of misc cleaning of the data
# input: the web data as a string, and each individual separated comment
# input: (functions for each comment are called in a loop until end of the file data)
# output: purify_web_data returns the web data string as a list of each separated comment
# output: the other 2 functions return each separated comment after performing some cleaning operation
import re
import html


def purify_web_data(web_data_string):
    # re.findall is used here to remove a lot of useless text and html data, but also
    # it returns each comment in a list, so the comments will next be purified individually
    cleaned_web_data = re.findall("<div class=\"md\">(.*?)</div>", web_data_string)
    return cleaned_web_data


def replacing_html_chars(comment_to_fix):
    comment_to_fix = comment_to_fix.replace("\\xe2\\x80\\x99", "’")  # left single quote
    comment_to_fix = comment_to_fix.replace("\\xe2\\x80\\x98", "‘")  # right single quote
    comment_to_fix = comment_to_fix.replace("\\xe2\\x80\\x9c", "“")  # left double quote
    comment_to_fix = comment_to_fix.replace("\\xe2\\x80\\x9d", "”")  # right double quote
    comment_to_fix = comment_to_fix.replace("\\xe2\\x80\\x94", "—")  # em dash
    comment_to_fix = comment_to_fix.replace("\\xe2\\x80\\xa6", "…")  # some other weird character
    return comment_to_fix


def purify_comment(comment):
    comment = re.sub("<.*?>", "", comment)  # removing html tags
    comment = html.unescape(comment)  # removing html escape characters
    comment = replacing_html_chars(comment)  # removing other escape characters
    comment = comment.replace("\\n", "\n")  # making the \n actually make newlines
    return comment
