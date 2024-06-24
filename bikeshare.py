#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np

## Import file to python

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
    
    city_valid = ['chicago','new york city','washington']
    
    while True:
        city = input('Please choose a city to analyze (chicago, new york city, washington): ').lower()
        if city not in city_valid:
            print ('Please input a valid city!')
        else:
                break

    # TO DO: get user input for month (all, january, february, ... , june)
    
    month_valid = ['january','february','march','april','may','june','all']
   
    while True:
        month = input("Please choose a month from january to june or type 'all':" ).lower()
        if month not in month_valid:
            print ('Please input a valid month!')
        else:
                break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day_valid = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
   
    while True:
        day = input("Please choose a day from monday to sunday or type 'all':" ).lower()
        if day not in day_valid:
            print ('Please input a valid day!')
        else:
                break
                
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
    
    # Load data file into data frame
    
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start Time column to datetime
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month from Start Time column
    
    df['month'] = df['Start Time'].dt.month_name().str.lower() 
    
     # Extract day from Start Time column
    
    df['weekday'] = df['Start Time'].dt.day_name().str.lower()
    
    # Filter by month
    
    if month != 'all':
        df = df[df['month'] == month]
    
    # Filter by day
    
    if day != 'all':
        df = df[df['weekday'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    most_common_month = df['month'].mode()[0]
    print ('The most common month of travel is ',most_common_month)


    # TO DO: display the most common day of week
    
    most_common_day = df['weekday'].mode()[0]
    print ('The most common day of travel is ',most_common_day)


    # TO DO: display the most common start hour
    
    ## Extract hour from Start Time column
    
    df['hour'] = df['Start Time'].dt.hour
    
    most_common_hour = df['hour'].mode()[0]
    print ('The most common hour of travel is ',most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    most_common_start_station = df['Start Station'].mode()[0]
    print ('The most common start station is ',most_common_start_station)


    # TO DO: display most commonly used end station
    
    most_common_end_station = df['End Station'].mode()[0]
    print ('The most common end station is ',most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    
    ## Combine Start Station and End Station

    df['journey'] = df['Start Station'] + ' - ' + df['End Station']
    
    most_common_journey = df['journey'].mode()[0]
    print ('The most common journey is ',most_common_journey)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is ', total_travel_time, ' seconds')

    # TO DO: display mean travel time
    
    avg_travel_time = df['Trip Duration'].mean()
    print('Average travel time is ', avg_travel_time, ' seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_type = df['User Type'].value_counts()
    print('Count of each user type:')
    print(user_type)

    # TO DO: Display counts of gender
    
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('Count of each gender:')
        print(gender)
    else:
        print('No data for gender.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print('Earliest year of birth is ',earliest_birth_year)
        print('Most recent year of birth is ',recent_birth_year)
        print('Most common year of birth is ',common_birth_year)
    else:
        print('No data for year of birth.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Show 5 first rows of raw data
    
def show_data(df):
    row_num = 0
    while True:
        show_data_option=input('\nWould you like to show 5 lines of raw data? (yes/no)').lower()
        if show_data_option == 'no':
            break
        else:
            print(df.iloc[row_num:row_num+5])
            row_num += 5
            if row_num > len(df):
               break 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




