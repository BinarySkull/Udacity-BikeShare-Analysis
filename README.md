# Udacity BikeShare Analysis

# Introduction

This project uses Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. It provides a command-line application that takes in user input and displays the result of descriptive statistics based on their input. The available statistics include popular times of travel, popular stations and trip, trip duration, and user information.The user can filter the data by city, month, and day, and then view statistics on the most common times of travel, the most popular stations and trips, the total and average trip duration, and the user demographics.

# Code Explanation

The code imports necessary libraries such as time, pandas, numpy, and math. It also defines a dictionary CITY_DATA that maps available cities to their corresponding CSV data files.

### get_filters function
This function prompts the user to enter a city, month, and day to analyze. It uses while loops to handle invalid inputs and returns the user's selections.

### load_data function
This function loads the bikeshare data from a CSV file into a pandas dataframe. It then filters the data by month and day if applicable.

### time_stats function
This function calculates and displays statistics on the most frequent times of travel, including the most common month, day of week, and start hour.

### station_stats function
This function calculates and displays statistics on the most popular stations and trips, including the most commonly used start and end stations and the most frequent combination of start station and end station trip.

### trip_duration_stats function
This function calculates and displays statistics on the total and average trip duration.

### user_stats function
This function calculates and displays statistics on bikeshare users, including the counts of user types and gender and the earliest, most recent, and most common birth years.

### show_row_data function
This function displays the raw data for the filtered data in 5-row increments. It uses a while loop to ask the user if they want to see more data and prints the result accordingly.

### main function
This function runs the program. It prompts the user for input, loads the data, and calls the other functions to display statistics. It also asks the user if they want to restart or exit the program.

# Conclusion
This project provides a powerful tool to analyze US bikeshare data and gain insights into popular times of travel, popular stations and trip, trip duration, and user information. By using descriptive statistics and a command-line interface, it provides a user-friendly way to interact with the data and gain insights into the bikeshare system.
#### ( The code could be found on Kaggle )
