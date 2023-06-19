import time
import pandas as pd
import numpy as np
import math

CITY_DATA = { 'CHICAGO': 'chicago.csv',
              'NEW YORK CITY': 'new_york_city.csv',
              'WASHINGTON': 'washington.csv' }
months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'ALL']



def get_filters():
        """
        Asks user to specify a city, month, and day to analyze.
        
        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
        print('Hello! Let\'s explore some US bikeshare data!')
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        
        while True:
            global city
            print('Enter a city from (chicago, new york city ,washington) that you want to get data about')
            city = input().upper()
            if  city == 'WASHINGTON' or city == 'NEW YORK CITY' or city == 'CHICAGO': 
                print('Ok, Please wait a moment')
                print()
                break
            else :
                print('Invalid input please try again and make sure the spelling is correct')
                                        
                                
                
                   
             
                
                # get user input for month (all, january, february, ... , june)
        while True:
            print('Which month do you need the data on?...(all, january , february , ... , june')
            month = str(input().upper())
            if  month == 'ALL' or month == 'JANUARY' or month == 'FEBRUARY' or month == 'MARCH' or month == 'April' \
                or month == 'MAY' or month == 'JUNE' or month == 'ALL':
                    print('Ok, Please wait a moment')
                    print()
                    break
            else : 
                    print('Invalid input please try again and make sure the spelling is correct')
                    
                
                
            
            # get user input for day of week (all, monday, tuesday, ... sunday)
        
        while True:
            print('Which day do you need the data on?...(all, monday, tuesday, ... sunday)')
            day = str(input().upper())
            if day == 'ALL' or day == 'SUNDAY' or day == 'MONDAY' or day == 'TUESDAY' or day == 'WEDNESDAY' \
                or day == 'THURSDAY' or day == 'FRIDAY' or day == 'SATURDAY' or day == 'ALL':
                    print('Ok, Please wait a moment')
                    print()
                    break
            else:
                print('Invalid input please try again and make sure the spelling is correct')
        print('-'*40)
                
        return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'ALL']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :{}".format(most_common_month))

    # display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :{}".format(most_common_day))

    # display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :{}".format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :{}".format( most_used_start_station))

    # display most commonly used end station
    most_used_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :{}".format(most_used_end_station))

    # display most frequent combination of start station and end station trip
    most_used_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}".format(most_used_start_end_station[0], most_used_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time :", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))
        
    while city != 'WASHINGTON':      
        '''Because washington doesn't have gender and birth year'''
        # Display counts of gender
        print("Counts of gender:\n")
        gender_counts = df['Gender'].value_counts()
        for index,gender_count   in enumerate(gender_counts):
            print("  {}: {}".format(gender_counts.index[index], gender_count))
        # Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year']
        most_common_year_of_birth = birth_year.value_counts().idxmax()
        print("The most common birth year:", most_common_year_of_birth)
        most_recent_year = birth_year.max()
        print("The most recent birth year:", most_recent_year)
        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year)
        break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_row_data(df):
    
    start=0
    ask= input('Do you want to show data (please answer with y or n)').upper()
    while ask == 'Y':
        print(df.iloc[start:start +5])
        start+=5
        ask= input('Would you like 5 more rows?').upper()
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
