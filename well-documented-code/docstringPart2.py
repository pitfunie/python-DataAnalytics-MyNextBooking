MyNextBooking LLC - Data Analysis Documentation

Overview

MyNextBooking LLC is a Tourism Startup aiming to provide the best booking experiences by analyzing the
number of distinct bookings, sessions, and searches from our datasets. This documentation provides a
step-by-step guide on how to analyze these datasets using Python and NumPy.


# This get_counts_by_day function is analyzing the combined dataset to count distinct bookings,
# sessions, and searches for each day of the week. This checks if the "search_time" column exists
# in the combined DataFrame. If it doesn't exist, the function returns an empty dictionary, as it
# can't perform the day-based analysis without timestamp information
def get_counts_by_day(self):
    if "search_time" not in self.df_combined.columns:
        return {}
    # it creates a new column called "day"
    self.df_combined["day"] = pd.to_datetime(
        self.df_combined["search_time"], format="ISO8601"
    ).dt.day_name()  # The format="ISO8601" parameter expects dates in ISO format (like "2023-12-25T10:30:00")
    # extracts the day name (Monday, Tuesday, etc.)
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    # # Group by day and count unique IDs
    counts = (  # Counts unique bookings, sessions, and searches for each day
        self.df_combined.groupby("day")  # Groups the data by day
        .agg(
            {
                "booking_id": "nunique",
                "session_id": "nunique",
                "search_id": (
                    "nunique"
                    if "search_id" in self.df_combined.columns
                    else "count"
                ),
            }
        )
        .reindex(days, fill_value=0)
    )
    # Returns the results as a dictionary where:
    return counts.to_dict(
        "index"
    )  # Values are dictionaries containing counts for bookings, sessions, and searches