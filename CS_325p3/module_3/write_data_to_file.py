
from CS_325p3.module_4.analyze_sentiment import get_sentiment
import os

def write_purified_data(file, output_file):
    list_of_analysis = []
    with open(file, "r", encoding="utf-8") as file:
        comments = file.read().split("\n")
        for comment in comments:
            if comment.strip() != "":
                comment_analysis = get_sentiment(comment)  # Passes comments to get_sentiment function
                if comment_analysis is not None:
                    list_of_analysis.append(comment_analysis + "\n") #samve the responses from openai to a list that will be stored in analyzed_site_data.txt
    
    with open(output_file, "w", encoding="utf-8") as output_file:
        output_file.writelines(list_of_analysis)
    
    print(f"Finished analyzing comments in file: {file}")


