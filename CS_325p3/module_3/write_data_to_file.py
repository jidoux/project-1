# this module writes the purified data, and also calls analyze_sentiment to use
# openai api to analyze the sentiment of each individual comment
# input: each comment, as a list, completely cleaned up
# output: writes the completely purified web data to a file, 1 comment at a time
from CS325_p3.module_4.analyze_sentiment import analyze_comments


def write_purified_data(cleaned_comments):  # this is kinda a mess, too many if statements, sorry
    num_iterations = 0
    num_comments_analyzed = 0
    list_of_analysis = []
    my_file = open("CS325_p3/Data/processed/processed_site_data.txt", "w", encoding="utf-8")
    for comment in cleaned_comments:
        if num_iterations > 2:  # Reddit has some default text on each page that this bypasses
            if comment.strip() != "[deleted]" and comment.strip() != "[removed]":  # removes deleted comments
                my_file.write(comment + "\n")
                if num_comments_analyzed < 50:  # because we have limited api calls, we limit them here
                    print(f"Analyzing comment #{num_comments_analyzed + 1}...")
                    comment_analysis = analyze_comments(comment, list_of_analysis)
                    # other error codes can happen like 502 or 503, and if so it returns empty string instead
                    if len(comment_analysis) != 0:
                        list_of_analysis.append(comment_analysis + "\n")
                        num_comments_analyzed += 1
        num_iterations += 1
    my_file2 = open("CS325_p3/Data/processed/analyzed_site_data.txt", "w", encoding="utf-8")
    my_file2.writelines(list_of_analysis)
    my_file2.close()
