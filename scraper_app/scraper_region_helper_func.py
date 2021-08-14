import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def scrape(link):
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

