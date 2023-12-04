# this module creates bar graphs to graph the sentiment analysis of each url
# input: the output file, bar graph title, and file number
# output: a bar graph displaying the sentiment analysis
import pandas as pd
from matplotlib import pyplot as plt


def generate_bar_graph(output_folder, bar_graph_title, file_num):
    # reading from the file, separated by a space, with no file header
    dataframe = pd.read_csv(f"{output_folder}/processed/analyzed_site_data/analyzed_site_data_{file_num}.txt", sep=" ", header=None)

    positive_count, negative_count, neutral_count = 0, 0, 0  # initializing these as 0 to ensure they are set
    # this is try catch block because if there is, for example, no positive sentiments, it would crash program
    # using 3 try catch blocks to check each individually, so if there are 50 negative sentiments only it still works
    try:
        positive_count = dataframe.value_counts()["Positive"]
    except Exception as e:
        print(f"There are no {str(e)} sentiments.")

    try:
        negative_count = dataframe.value_counts()["Negative"]
    except Exception as e:
        print(f"There are no {str(e)} sentiments.")

    try:
        neutral_count = dataframe.value_counts()["Neutral"]
    except Exception as e:
        print(f"There are no {str(e)} sentiments.")

    sentiments = ["Positive", "Negative", "Neutral"]  # these label the bars themselves
    sentiment_counts = [positive_count, negative_count, neutral_count]  # this sets how high the bars will be
    bar_labels = ['Positive', "Negative", "Neutral"]  # this labels the legend
    bar_colors = ['red', 'blue', 'green']  # this dictates the color of each bar, can be any color

    figure, axis = plt.subplots()  # I don't know what this does but its necessary

    axis.bar(sentiments, sentiment_counts, label=bar_labels, color=bar_colors)  # Creates the bar chart

    axis.set_ylabel("Number of each sentiment")
    axis.set_title(bar_graph_title)
    axis.legend(title="Sentiment colors")

    # saving the plot in the output folder Plots
    plt.savefig(f"{output_folder}/Plots/bar_graph_{file_num}")
