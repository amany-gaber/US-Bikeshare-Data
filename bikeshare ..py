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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like shaw the data for chicago , new york city or washington : ').lower() 
    while city not in CITY_DATA.keys() :
        print('Invalid city name')
        city = input('Would you like shaw the data for chicago , new york or washington : ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all' ]
    month = input('Would you like to filter data in specific month or all months : ').lower()
    while month not in months :
        print('Invalid month name')
        month = input('Would you like to filter data in specific month or all months : ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days  =['saturday','sunday' , 'monday' , 'tuesday', 'wednesday', 'thursday', 'friday' , 'all' ]
    day = input('Would you like to filter data in specific day or all days : ').lower()
    while day not in days :
        print('Invalid day name')
        day = input('Would you like to filter data in specific day or all days : ').lower()


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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
    # filter month or day 
    if month != 'all' :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # create data frame for this month 
        df = df[df['month'] == month ] 

    if day != 'all' :
        df = df[df['day_of_week'] == day.title() ]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    pop_month = df['month'].mode()[0]
    print('Most common month : ', months[pop_month-1] )
          
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day  : ', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    pop_hour = df['hour'].mode()[0]
    print('Most common start hour : ' , pop_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station :' , pop_start_station)
          
    # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station :' , pop_end_station)
       

    # TO DO: display most frequent combination of start station and end station trip
    pop_trip_comb = (df['Start Station'] + 'to' + df['End Station']).mode()[0]
    print('Most frequent combination :' , pop_trip_comb )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time :' , total_travel_time/86400 ,'days' )

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time :' , mean_travel_time/60 , ' minutes' )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('Counts of user types :')
    print(count_user_type)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns :
          counts_gender = df['Gender'].value_counts()
          print ('Counts of gender')
          print(counts_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns :
          print('Earliest year : ' , int(df['Birth Year'].min()))
          print('Most recent year : ' , int(df['Birth Year'].max()))
          print('Most common year : ' , int(df['Birth Year'].mode()[0]))
                

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   
def display_raw_data(df):
    raw = input('\nWould you like to diplay raw data?\n')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            ask = input('Next 5 raws?')
            if ask.lower() != 'yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
