from matplotlib import pyplot as plt

class BarGraph:
# Enter the data you are going to use and the title of the graph
    def init_Creat_BarGraph(self, x_axies, y_axies, Title):
        fig, ax = plt.subplots(figsize =(40, 20))
 
        # Horizontal Bar Plot
        ax.barh(x_axies,y_axies)
 
        # Remove axes splines
        for s in ['top', 'bottom', 'left', 'right']:
            ax.spines[s].set_visible(False)
 
        # Remove x, y Ticks
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')
 
        # Add padding between axes and labels
        ax.xaxis.set_tick_params(pad = 5)
        ax.yaxis.set_tick_params(pad = 10)
 
        # Add x, y gridlines
        ax.grid(b = True, color ='grey',
               linestyle ='-.', linewidth = 0.5,
                alpha = 0.2)
 
        # Show top values
        ax.invert_yaxis()
        plt.rcParams.update({'font.size': 25})

        # Sets the x and y lables
        ax.set_ylabel('Artists')
        ax.set_xlabel('Popularity(Millions)')

        # Add annotation to bars
        for i in ax.patches:
         plt.text(i.get_width()+0.2, i.get_y()+0.5,
                 str(round((i.get_width()), 2)),
                 fontsize = 10, fontweight ='bold',
                 color ='grey')
 
        # Add Plot Title
        ax.set_title(Title,
                 loc ='left', )
 
        # Add Text watermark
        fig.text(0.9, 0.15, 'CS_Class', fontsize = 10,
             color ='grey', ha ='right', va ='bottom',
             alpha = 0.7)
 
        # Show Plot
        Title += '.png'
        plt.savefig('{}/{}'.format('img', Title))
    