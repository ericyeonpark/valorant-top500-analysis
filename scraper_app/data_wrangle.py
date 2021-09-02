import pandas as pd
from sklearn.model_selection import train_test_split
file = '2021-03-21_2157_Val_Top500_Stats'


def wrangle(data):
    '''
    Import Val Top 500 csv and clean to create a dataframe
    appropriate for modeling
    '''

    # Create column names
    col_names = ['Rank', 'Player', 'Rating', 'Winrate', 'Games',
                'Average_Score', 'Head_Shot_Pct', 'Class', 'Region']

    # import data into df
    df = pd.read_csv(data, columns=col_names)

    # remove spaces and symbols
    df['Winrate'] = df['Winrate'].str.replace('%', '')
    df['HS%'] = df['HS%'].str.replace('%', '')
    df['Avg.Score'] = df['Avg.Score'].str.replace(',', '')

    # convert numeric strings to floats or ints
    df['Winrate'] = df['Winrate'].astype('float')
    df['HS%'] = df['HS%'].astype('float')
    df['Avg.Score'] = df['Avg.Score'].astype('float')
    df['Rank'] = df['Rank'].astype('int32')

    # # drop irrelevant, bugged columns
    df.drop(columns = ['Most Agents'], inplace = True)

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
