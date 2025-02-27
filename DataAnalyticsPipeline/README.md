MyNextBooking LLC: Competitor App Analytics

Overview: MyNextBooking LLC is a ticket booking app that helps users compare ticket prices for their upcoming journeys. The platform collects and analyzes booking and session data to provide insights into user behavior and trends. This analysis focuses on competitor applications across various devices such as iOS, Android, Desktop, and Laptop, with a particular emphasis on consumer search behaviors.

Objective:

    Analyze the provided datasets (bookings.csv and sessions.csv) to determine the number of distinct bookings, sessions, and searches.

    Utilize data analysis libraries such as NumPy and Pandas, along with visualization tools like Matplotlib, to extract and present the required insights.

Instructions for Analysis:

    Import Libraries:

        Import the necessary libraries: NumPy, Pandas, and Matplotlib.
    python

    import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Load Datasets:

    Load the datasets bookings.csv and sessions.csv into DataFrames.

python

bookings_df = pd.read_csv('bookings.csv')
sessions_df = pd.read_csv('sessions.csv')

Data Cleaning and Preprocessing:

    Clean and preprocess the data as required. This may include handling missing values, converting data types, and removing duplicates.

python

distinct_bookings = bookings_df['booking_id'].nunique()
distinct_sessions = sessions_df['session_id'].nunique()
distinct_searches = sessions_df['search_id'].nunique()

Compute Distinct Values:

    Compute the number of distinct bookings, sessions, and searches.

Visualize Results:

    Visualize the results using Matplotlib to present the data clearly.

python

labels = ['Bookings', 'Sessions', 'Searches']
values = [distinct_bookings, distinct_sessions, distinct_searches]

plt.bar(labels, values)
plt.xlabel('Categories')
plt.ylabel('Count')
plt.title('Distinct Bookings, Sessions, and Searches')
plt.show()


Additional Insights:

    Session Analysis: Identify sessions with multiple bookings and analyze user interactions by merging datasets when necessary.

    Booking Trends: Determine the most popular booking days and visualize them with a pie chart.

    Device Usage: Analyze the most used device types for making bookings on the platform and plot trends at a quarterly frequency.

Example Outputs:

    Pie chart of bookings by day.

    Total number of unique bookings and sessions.

    Analysis of sessions with multiple bookings.

    Heatmap displaying correlations of numerical columns in the bookings dataset.

Technologies Used:

    Python

    Pandas (for data manipulation)

    Matplotlib & Seaborn (for data visualization)

    Jupyter Notebook (for interactive analysis)
