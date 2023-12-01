import pandas as pd
from matplotlib import pyplot as plt


def generate_bar_graph(output_folder, file_num):
    # reading from the file, separated by a space, with no file header
    dataframe = pd.read_csv(f"{output_folder}/processed/analyzed_site_data/analyzed_site_data_{file_num}.txt", sep=" ",header=None)

    positive_count = dataframe.value_counts()["Positive"]
    negative_count = dataframe.value_counts()["Negative"]
    neutral_count = dataframe.value_counts()["Neutral"]

    # these 3 lines are testing lines, maybe delete before final submission, or maybe not
    print(f"Positive count is {positive_count}")
    print(f"Negative count is {negative_count}")
    print(f"Neutral count is {neutral_count}")

    sentiments = ["Positive", "Negative", "Neutral"]  # these label the bars themselves
    sentiment_counts = [positive_count, negative_count, neutral_count]  # this sets how high the bars will be
    bar_labels = ['Positive', "Negative", "Neutral"]  # this labels the legend
    bar_colors = ['red', 'blue', 'green']  # this dictates the color of each bar, can be any color

    figure, axis = plt.subplots()  # I don't know what this does but its necessary

    axis.bar(sentiments, sentiment_counts, label=bar_labels, color=bar_colors)  # Creates the bar chart I think?

    axis.set_ylabel("Number of each sentiment")
    axis.set_title("Sentiments")  # TODO: change this to reddit post name
    axis.legend(title="Sentiment colors")

    plt.show()  # shows the bar chart on the screen, I guess when project is finalized this isn't needed?
