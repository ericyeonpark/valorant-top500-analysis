import pandas as pd
from sklearn.model_selection import train_test_split
file = '2021-03-21_2157_Val_Top500_Stats'


def wrangle(df):
    '''
    Wrangle the dataframe created by the scraping function. 
    Rename columns to match database
    Removed unnessary strings from HeadShot%, Winrate, Average_Score
    Changed columns to match database architecture
    '''

    # Create column names
    col_names = ['Rank', 'Player', 'Rating', 'Winrate', 'Games',
                'Average_Score', 'Head_Shot_Pct', 'Class', 'Region']

    # rename the columns in the df
    df.rename(columns={'Avg.Score':'Average_Score', 'HS%':'Head_Shot_Pct'}, inplace=True)

    # #remove spaces and symbols
    df['Winrate'] = df['Winrate'].str.replace('%', '')
    df['Head_Shot_Pct'] = df['Head_Shot_Pct'].str.replace('%', '')
    df['Average_Score'] = df['Average_Score'].str.replace(',', '')

    # convert numeric strings to floats or ints
    df['Winrate'] = df['Winrate'].astype('float')
    df['Head_Shot_Pct'] = df['Head_Shot_Pct'].astype('float')
    df['Average_Score'] = df['Average_Score'].astype('int64')
    df['Rating'] = df['Rating'].astype('float')
    df['Rank'] = df['Rank'].astype('int32')
    df['Games'] = df['Games'].astype('int32')

    # convert series to strings
    df['Player'] = df['Player'].astype('string')
    df['Region'] = df['Region'].astype('string')
    df['Class'] = df['Class'].astype('string')

    return df


def train_test_split():
    '''Create a train test 75:25 split'''
    # Create X and y(target) variables based off of df
    target = 'Rating'
    X = df.drop(columns = target)
    y = df[target]


    # Train test split the X and y datasets 
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y, 
                                                        test_size=0.25,
                                                        random_state=42)


    return X_train, X_test, y_train, y_test
