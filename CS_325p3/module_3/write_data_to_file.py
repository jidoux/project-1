# this module writes the purified data, and also calls get_sentiment to analyze sentiments
# input: the file of purified web data, and the output file
# output: writes the sentiment analysis to output file
from CS_325p3.module_4.analyze_sentiment import get_sentiment


def write_purified_data(file, output_file):
    list_of_analysis = []
    num_comments_analyzed = 0
    with open(file, "r", encoding="utf-8") as file:
        comments = file.read().split("\n")
        print("Analyzing a reddit post:")
        for comment in comments:
            if comment.strip() != "" and num_comments_analyzed < 50:  # this limits the number of api calls
                print(f"Analyzing comment #{num_comments_analyzed + 1}...")
                comment_analysis = get_sentiment(comment)  # Passes comments to get_sentiment function
                num_comments_analyzed += 1
                print(num_comments_analyzed)
                if comment_analysis is not None:
                    list_of_analysis.append(
                        comment_analysis + "\n")  # save the responses from openai to a list that will be stored in
                    # analyzed_site_data.txt

    with open(output_file, "w", encoding="utf-8") as output_file:
        output_file.writelines(list_of_analysis)

    print("Finished analyzing a reddit post!")
