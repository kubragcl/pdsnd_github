import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    city = input("Please write a city to learn more about data in Chicago, New York City or Washington: ").lower()

    #a while loop to handle invalid city names
    while city not in (CITY_DATA.keys()):
        print("Please be sure not choosing an invalid city name")
        city = input("Write a city to learn more about data in Chicago, New York City or Washington: ").lower()

    #Asks users the filter type
    filter = input('Would you like to filter the data by month, day, both, or none? ').lower()
    while filter not in(['month', 'day', 'both', 'none']):
        print('You provided invalid filter')
        filter = input('Would you like to filter the data by month, day, both, or none? ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["all", "january", "february", "march", "april", "may", "june"]
    if filter == "month" or filter == "both":
        month = input("Which month - January, February, March, April, May, or June: ").lower()
        while month not in months:
            print("You provided invalid month.")
            month = input("Which month - January, February, March, April, May, June: ").lower()
    else:
        month = "all"

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if filter == "day" or filter == "both":
        day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ").title()
        while day not in days:
            print("You provided invalid day")
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ").title()
    else:
        day = "all"

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
    #convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #convert to the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month from the Start Time column
    df['month'] = df['Start Time'].dt.month

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month: ", common_month)

    #extract day from the Start Time column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week: ", common_day)

    #extract hour from the Start Time column
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour: ", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_trip = df['Start Station'] + ' to ' + df['End Station']
    print(f'The most popular trip is: from {most_frequent_trip.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    print('\n\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    print('\n\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        year = df['Birth Year'].fillna(0).astype('int64')
        print(
            f'Earliest birth year is: {year.min()}\nmost recent is: {year.max()}\nand most common birth year is: {year.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Display data if user wants to see"""
    #ask for raw data first 5 and then next 5 raw data rows
    while True:
        view_input_five = input('\nWould you like to see first 5 rows of data? Please enter yes or no:').lower()
        if view_input_five in ('yes'):
            n = 0
            print(df.iloc[n:n+5])
        n += 5
        break
    while True:
        view_more_data = input('Would you like to see next 5 rows of data? Please enter yes or no:').lower()
        if view_more_data != ('yes'):
            m = 1
            print(df.iloc[m:m+10])
        m += 20
        break
        print(view_more_data)
    return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
