# this module cleans the raw website data
# input: the raw web data, in the form of some BeautifulSoup object
# output: a list of each cleaned comment


def purify_web_data(web_data):
    cleaned_comments = [comment.text for comment in web_data.find_all('div', attrs={'class': 'md'})]
    return cleaned_comments
