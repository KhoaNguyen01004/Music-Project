import matplotlib.pyplot as plt
import itertools
import numpy as np

class MatPlotLibHandler:


    def plot(self, graph_file_name, x, y, title, x_label, y_label):
        """
        Description:
        ------------
        Plots out the view count of each video in the playlist into a bar graph.
        """
        fig, ax = plt.subplots(figsize=(40, 10))
        ax.bar(x, y)
        plt.xticks(rotation=90)
        plt.xlabel(x_label)#Video Title
        plt.ylabel(y_label)#View Count (in hundred millions)
        plt.title(title)#Current Popular Songs on YouTube and Their View Counts
        plt.savefig('{}/{}'.format('img', graph_file_name), bbox_inches = 'tight')
        plt.close()

    def plot_two(self, graph_file_name, data_one_x, data_one_y, data_two_x, data_two_y, legend, title, x_label, y_label):
        """
        Description:
        ------------
        Plots out a comparison of Global and US top songs on Youtube.
        """
        combined_x = [x for x in itertools.chain.from_iterable(itertools.zip_longest(data_one_x, data_two_x)) if x]
        bar_pos = np.arange(len(combined_x))
        combined_y = [x for x in itertools.chain.from_iterable(itertools.zip_longest(data_one_y, data_two_y)) if x]
        color_one = ['red' for _ in range(len(data_one_x))]
        color_two = ['blue' for _ in range(len(data_two_x))]
        combined_color = [x for x in itertools.chain.from_iterable(itertools.zip_longest(color_one, color_two)) if x]
        fig, ax = plt.subplots(figsize=(40, 10))
        ax.bar(bar_pos, combined_y, color = combined_color)
        ax.bar(bar_pos, combined_y, color = combined_color)
        ax.legend(legend)
        leg = ax.get_legend()
        leg.legendHandles[0].set_color('red')
        leg.legendHandles[1].set_color('blue')
        plt.xticks(bar_pos, combined_x, rotation=90)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.savefig('{}/{}'.format('img', graph_file_name), bbox_inches = 'tight')
        plt.close()
