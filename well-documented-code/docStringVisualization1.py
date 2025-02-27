MyNextBooking LLC - Data Analysis Documentation

Overview

MyNextBooking LLC is a Tourism Startup aiming to provide the best booking experiences by analyzing the
number of distinct bookings, sessions, and searches from our datasets. This documentation provides a
step-by-step guide on how to analyze these datasets using Python and Matplotlab.p.


# Visualizer class is responsible for creating a 3D bar plot to visualize the data analyzed by the
# DataAnalyzer class. Let's break down its structure and functionality:
class Visualizer:
    def __init__(self, data):
        self.data = data

    def plot_3d_bar(self):
        # The plot_3d_bar method creates the 3D bar plot.
        # Setting up the plot: Creates a new figure with a specified size. Adds a 3D subplot to
        # this figure.
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')

        days = list(self.data.keys())
        categories = ['booking_id', 'session_id', 'search_id']
        # Creating the grid for the 3D plot:
        x = np.arange(len(days))
        y = np.arange(len(categories))
        # meshgrid to create 2D arrays from these 1D arrays, which is necessary for 3D plotting.
        x, y = np.meshgrid(x, y)
        # Creating the data array
        z = np.array([[self.data[day][cat] for day in days] for cat in categories])

        dx = 0.75  # width of bars
        dy = 0.75  # depth of bars
        dz = z.flatten()  # # heights of bars (flattens 2D array to 1D)

        colors = ["r", "g", "b"]  # red, green, blue for different categories

        for i in range(len(x.flat)):
            ax.bar3d(
                x.flat[i],  # x coordinate
                y.flat[i],  # y coordinate
                0,  # starting height (base of bar)
                dx,  # width
                dy,  # depth
                dz[i],  # height of bar
                color=colors[i % len(colors)],  # cycles through colors
                alpha=0.8,  # transparency
            )
        # Rows represent categories (Bookings, Sessions, Searches)
        ax.set_xticks(np.arange(len(days)))
        ax.set_yticks(np.arange(len(categories)))
        ax.set_yticklabels(['Bookings', 'Sessions', 'Searches'])

        ax.set_xlabel('Days')
        # labelpad=20 parameter to set_ylabel. This will increase the distance between
        # the y-axis label and the y-axis tick labels. You can adjust the value of labelpad to increase
        # r decrease the distance as needed.
        ax.set_ylabel('Categories', labelpad=15)
        # Sets the label for the z-axis to "Count"
        ax.set_zlabel('Count')
        ax.set_title('Distinct Bookings, Sessions, and Searches by Day')
        # Creates a legend for the plot. handles=[plt.Rectangle((0,0),1,1,color=c,alpha=0.8) for
        # c in colors] creates colored rectangles for each category in the legend. l
        # abels=['Bookings', 'Sessions', 'Searches'] sets the text for each item in the legend.
        plt.legend(handles=[plt.Rectangle((0,0),1,1,color=c,alpha=0.8) for c in colors],
                   labels=['Bookings', 'Sessions', 'Searches'], loc='upper left', bbox_to_anchor=(1.1, 1))
        # Adjusts the padding between and around subplots to minimize overlaps.
        plt.tight_layout()
        plt.show()
# The main() function serves as the entry point of the program and orchestrates the overall flow of
# the data analysis and visualization process.
def main():
    # Creates an instance of the DataAnalyzer class, passing the names of two CSV files: "Bookings.csv"
    # and "Sessions.csv".
    analyzer = DataAnalyzer("Bookings.csv", "Sessions.csv")
    # Calls the get_distinct_counts() method of the analyzer to get the number of distinct bookings,
    # sessions, and searches.
    distinct_counts = analyzer.get_distinct_counts()
    # print distinct counts: This line prints the distinct counts for bookings, sessions, and searches
    print("Distinct Counts:")
    for category, count in distinct_counts.items():
        print(f"{category}: {count}")
    # Calls the get_counts_by_day() method to get the counts of bookings, sessions, and searches for
    # each day of the week.
    counts_by_day = analyzer.get_counts_by_day()
    # Visualization check and execution
    if counts_by_day:
        visualizer = Visualizer(counts_by_day)
        visualizer.plot_3d_bar()
    else:
        print("No data available for visualization.")
'''
The primary purpose to control the execution of code blocks, ensuring they only run
when a script is executed directly, not when it's imported aas a module
'''
if __name__ == "__main__":
    main()