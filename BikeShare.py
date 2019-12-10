import time
import pandas as pd
import numpy as np
# import datetime as d
# from time import strptime
from datetime import datetime
from time import strptime


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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city= str(input('Enter a city (chicago - new york city - washington): ')).lower()
    while city not in CITY_DATA:
        print("Incorrect input, choose only one of these 3 cities (chicago - new york city - washington).")
        city= str(input('Enter a city (chicago - new york city - washington): ')).lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month= str(input('Enter a month to filter by (all OR months from january to june): ')).lower()
    
    while month not in ('january', 'february', 'march', 'april', 'may' , 'june', 'all'):
        print("Incorrect input, choose only one of these choices (all OR months from january to june).")
        month= str(input('Enter a month to filter by (all OR from january to june): ')).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day= str(input('Enter a day of week (all OR days from monday to sunday): ')).lower()
    while day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday' , 'saturday','sunday','all'):
         print("Incorrect input, choose only one of these choices (all OR days from monday to sunday).")
         day= str(input('Enter a day of week (all OR days from monday to sunday): ')).lower()


        
        
        
    print('-'*40)
    return city, month, day



def month_string_to_number(string):
    m = {
        'january' : 1,
        'february' : 2,
        'march' : 3,
        'april' : 4,
        'may' : 5,
        'june' : 6,
        'july' : 7,
        'august' : 8,
        'september' : 9, 
        'october' : 10,
        'november' : 11,
        'december' : 12
    }
    s = string.strip()[:3].lower()
    
def day_string_to_number(string):
    m = {
        'monday' : 0,
        'tuesday' : 1,
        'wednesday' : 2,
        'thursday' : 3,
        'friday' : 4,
        'saturday' : 5,
        'sunday' : 6
  }
    s = string.strip()[:3].lower()




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
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.dayofweek
    

    
    if month != 'all':
        df["Month"] == month_string_to_number(month)




    if day != 'all':
        df["Day"] == day_string_to_number(day)


        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    print("The most common month: ",df['Month'].mode()[0])

    
    # TO DO: display the most common day of week
    
    print("The most common day of week: ",df['Day'].mode()[0])
    # TO DO: display the most common start hour
    df['Hour'] = pd.to_datetime(df['Start Time']).dt.hour
    print("The most common start hour: ",df['Hour'].mode()[0])
        
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    print('Most commonly used start station: ',df['Start Station'].mode()[0])
    
    # TO DO: display most commonly used end station

    print('Most commonly used end station: ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("Most common trip from start to end: ",(df['Start Station'] + ", " + df['End Station']).mode()[0])
                                            

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    print('Total travel time: ',df['Trip Duration'].sum())
    
    # TO DO: display mean travel time
    print('Mean of travel time: ',df['Trip Duration'].mean())

    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print('Counts of user types: ',df['User Type'].value_counts())
    
    
    
    
    
    if "Gender" and "Birth Year" in df:
        # TO DO: Display counts of gender
        print('Counts of gender: ',df['Gender'].value_counts())
        
        # TO DO: Display earliest, most recent, and most common year of birth
         #Earliest:
        print('Earliest year of birth: ',df.min()['Birth Year'])
        #Recent:
        print('Most recent year of birth: ',df.max()['Birth Year'])
        #Most common:
        print('Most common year of birth: ',df['Birth Year'].mode()[0])

    else:
        print("** Sorry, the city doesn't have a gender/year of birth coloumn.. **")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

       
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        
        ask1=input('\nWould you like to see the first 5 lines? Enter yes or no.\n')
        if ask1 == 'yes':
            data = pd.read_csv(CITY_DATA[city])
            i = 0
            j=4


            print(data.loc[i:j, :])

        else:
            break
            
        
        while True:
            
            ask2 = input('\nWould you like to see more? Enter yes or no.\n')
            if ask2.lower() != 'yes':
                break
                
            else:
                i = i + 5
                j = j + 5
              
                
                print(data.loc[i:j, :])

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

       

if __name__ == "__main__":
	main()
