MyNextBooking LLC - Data Analysis Documentation

Overview

MyNextBooking LLC is a Tourism Startup aiming to provide the best booking experiences by analyzing the
number of distinct bookings, sessions, and searches from our datasets. This documentation provides a
step-by-step guide on how to analyze these datasets using Python and NumPy.



# This code block is importing various Python libraries and modules that are commonly used
# for data manipulation, analysis, and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D is importing the Axes3D class from the mpl_toolkits.mplot3d
# to creating 3D plots in Matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Class is designed to load, merge, and analyze data from two CSV files: one for bookings
# and one for sessions.
class DataAnalyzer:
    # Initialization ( __init__ method):
    # It takes two parameters: bookings_file and sessions_file, which are the filenames of the CSV files
    # containing booking and session data.
    def __init__(self, bookings_file, sessions_file):
        # It reads these CSV files into pandas DataFrames: [1] self.df_bookings contains the data from
        # the bookings file self.df_sessions contains the data from the sessions file
        self.df_bookings = pd.read_csv(bookings_file)
        self.df_sessions = pd.read_csv(sessions_file)
        self.df_combined = self.merge_dataframes()
    # Uses pd.merge() with the following parameters: on="booking_id": This specifies that the DataFrames
    # should be merged based on the "booking_id" column, which is assumed to be present in both DataFrames.
    # how="outer": This performs an outer join, which means all records from both DataFrames are kept,
    # even if they don't have a matching "booking_id" in the other DataFrame. Missing values are filled
    # with NaN.
    def merge_dataframes(self):
        return pd.merge(
            self.df_bookings, self.df_sessions, on="booking_id", how="outer"
        )
    # The get_distinct_counts function is calculating and returning the number of unique (distinct)
    # values for bookings, sessions, and searches in the combined dataset.
    def get_distinct_counts(self):
        # distinct_bookings = self.df_combined["booking_id"].nunique() This counts the number of unique
        # values in the "booking_id" column of the combined DataFrame. nunique() is a pandas method that
        # returns the number of unique elements in a Series.
        distinct_bookings = self.df_combined["booking_id"].nunique()
        # distinct_sessions = self.df_combined["session_id"].nunique()Similarly, this counts the number
        # of unique values in the "session_id" column.
        distinct_sessions = self.df_combined["session_id"].nunique()
        # distinct_searches the conditional statement: It first checks if the "search_id" column exists
        # in the combined DataFrame. If it exists, it counts the number of unique values in the
        # "search_id" column.
        distinct_searches = (
            self.df_combined["search_id"].nunique()
            if "search_id" in self.df_combined.columns
            else 0
        )

        return {
            "Bookings": distinct_bookings,
            "Sessions": distinct_sessions,
            "Searches": distinct_searches,
        }