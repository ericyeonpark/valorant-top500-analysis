import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def wrangle(link):
    '''
    scrape Valorant stats from the Top 500 players in 
    (Korea, EU, Asian Pacific, BR, LATAT)
    Data from dak.gg/valorant/leaderboard and updated as of 2021-03-22
    Data links are found in dak_links.py
    '''
    #Load the webpage content
    r = requests.get(link)

    #Convert to a beautiful soup object
    soup = bs(r.content) 

    #Extract column names from table
    table = soup.select('table.stats-table')[0]
    columns = table.find('thead').find_all('th')
    column_names = [c.string for c in columns]

    #Extract table rows
    table_rows = table.find('tbody').find_all('tr')
    
    #Create dataframe
    l = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [str(tr.get_text()).strip() for tr in td]
        l.append(row)

    df = pd.DataFrame(l, columns = column_names)

    return df



def create_final_DF(df_NA, df_EU, df_KR, df_BR, df_LA, df_AP):
    '''
    Combine all the created DF's for each region into one combined df
    '''
    df_final = pd.concat([df_NA, 
                df_EU,
                df_KR, 
                df_BR, 
                df_LA, 
                df_AP])

    return df_final