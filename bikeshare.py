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
    city = input('Please, type in the name of the city you will like to explore; chicago, new york city or washington: \n').lower()
    while (city not in (CITY_DATA).keys()):
        print('\nPlease, enter an appropriate selection from the options available!')
        city = input('Please, type in the name of the city you will like to explore; chicago, newyork or washington: \n').lower()
        break


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nWhich month are you interested in exploring? (all, January, February, March, April, May, June)\nPlease, type all if you are interested in exploring all available months: ').title()
    if month not in ('All', 'January', 'February', 'March', 'April', 'May', 'June'):
        print('\nPlease, enter a valid selection!')
        month = input('\nWhich month are you interested in exploring? (all, January, February, March, April, May, June)\nPlease, type all if you are interested in exploring all available months: ').title()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWhat day are you interested in exploring? (all, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)\n Please, type all if you are interested in exploring all days: ').title()
    if day not in ('All', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
        print('\nPlease, check your entry and try again!')

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('\nThe most popular month for travel is: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('\nThe most popular day for travel is: ', popular_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nThe most popular hour for travel is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nThe most popular start station is: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nThe most popular end station is: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Frequent Trip'] = df['Start Station'] + " and " + df['End Station']
    popular_trip = df['Frequent Trip'].mode()[0]
    print('\nThe stations with the most frequent start and end trips are: ', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time is: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('\nThe counts of user types is: \n', user_types_count)

    # TO DO: Display counts of gender
    cities = ['chicago', 'new york city', 'washington']
    for city in cities:
        if 'Gender' in df.columns:
            gender_count = df['Gender'].value_counts()
            print('\nThe gender count is: \n', gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
            earliest_birth_year = df['Birth Year'].min()
            print('\nThe earliest year of birth is: ', earliest_birth_year)
            most_recent_birthyear = df['Birth Year'].max()
            print('\nThe most recent year of birth is: ', most_recent_birthyear)
            popular_birth_year = df['Birth Year'].mode()[0]
            print('\nThe most popular year of birth is: ', popular_birth_year)
        else:
            print('\nThe gender and year of birth for this data are not available!')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def raw_data_input(city):
    """ Display five rows of raw data if the user if they want to explore the raw data """
    index = 0
    n_rows = 5
    while True:
        raw_data_input = input('\nIf you would like to explore the raw data and see 5 rows at a time, enter yes or no: \n')
        if raw_data_input == 'yes':
            df = pd.read_csv(CITY_DATA[city], na_filter=False)
            print(df.iloc[index*n_rows:(index + 1)*n_rows])
            index += 1
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_input(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
