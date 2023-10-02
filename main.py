import urllib.request
import sys
import re
import html


# Replacing these sequences.
def replacing_html_chars(comment_to_fix):
    comment_to_fix = comment_to_fix.replace("\\xe2\\x80\\x99", "’")  # left single quote
    comment_to_fix = comment_to_fix.replace("\\xe2\\x80\\x98", "‘")  # right single quote
    comment_to_fix = comment_to_fix.replace("\\xe2\\x80\\x9c", "“")  # left double quote
    comment_to_fix = comment_to_fix.replace("\\xe2\\x80\\x9d", "”")  # right double quote
    comment_to_fix = comment_to_fix.replace("\\xe2\\x80\\x94", "—")  # em dash
    comment_to_fix = comment_to_fix.replace("\\xe2\\x80\\xa6", "…")  # some other weird character
    return comment_to_fix


web_data = urllib.request.urlopen(sys.argv[1])
web_data_string = ""
web_data_string += str(web_data.read())
my_file = open("site_content.txt", "w", encoding="utf-8")
cleaned_web_data = re.findall("<div class=\"md\">(.*?)</div>", web_data_string)
num_iterations = 0
for comment in cleaned_web_data:
    if num_iterations > 2: # Reddit has some default text on each page that this bypasses
        comment = re.sub("<.*?>", "", comment)  # removing html tags
        comment = html.unescape(comment)  # removing html escape characters
        comment = replacing_html_chars(comment)  # removing other escape characters
        comment = comment.replace("\\n", "\n") # making the \n actually make newlines
        my_file.write(comment + "\n")
    num_iterations += 1
