# this module writes the purified data
# input: each comment, as a list, completely cleaned up
# output: writes the completely purified web data to a file, 1 comment at a time


def write_purified_data(cleaned_comments):
    num_iterations = 0
    my_file = open("CS325_p3/Data/processed/processed_site_data.txt", "w", encoding="utf-8")
    for comment in cleaned_comments:
        if num_iterations > 2:  # Reddit has some default text on each page that this bypasses
            if comment.strip() != "[deleted]" and comment.strip() != "[removed]":  # removes deleted comments
                my_file.write(comment + "\n")
        num_iterations += 1
