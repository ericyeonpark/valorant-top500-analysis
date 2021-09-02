import requests
import os
import dataset
from bs4 import BeautifulSoup as bs
import pandas as pd


from sqlalchemy.exc import ProgrammingError
from dotenv import load_dotenv
import psycopg2


# import functions and code from other py files
import dak_links
from data_wrangle import wrangle


# import BD url from .env file
load_dotenv()

# make database connection
db = dataset.connect(os.getenv("DB_URL"))

def final_scrape():
    '''
    Use each individual scraping functions to scrape Valorant stats from the Top 500 players in the 6 major 
    regions of Valorant
    '''
    
    # connect to database
    db = dataset.connect(os.getenv("DB_URI"))
    table = db["first_test"]
    conn = psycopg2.connect(os.getenv("DB_URI"))
    curs = conn.cursor()
    conn.commit()


    # Get links to scrape
    kr_link1, kr_link2, kr_link3, kr_link4, kr_link5, \
        kr_link6, kr_link7, kr_link8, kr_link9, kr_link10 = create_link_kr()

    eu_link1, eu_link2, eu_link3, eu_link4, eu_link5, \
        eu_link6, eu_link7, eu_link8, eu_link9, eu_link10 = create_link_eu()

    na_link1, na_link2, na_link3, na_link4, na_link5, \
        na_link6, na_link7, na_link8, na_link9, na_link10 = create_link_na()

    ap_link1, ap_link2, ap_link3, ap_link4, ap_link5, \
        ap_link6, ap_link7, ap_link8, ap_link9, ap_link10 = create_link_ap()

    br_link1, br_link2, br_link3, br_link4, br_link5, \
        br_link6, br_link7, br_link8, br_link9, br_link10 = create_link_br()

    la_link1, la_link2, la_link3, la_link4, la_link5, \
        la_link6, la_link7, la_link8, la_link9, la_link10 = create_link_la()


    # Scrape using scraping functions in scraper.py
    df_KR = scrape_kr(link1 = kr_link1, link2 = kr_link2, 
                    link3 = kr_link3, link4 = kr_link4, 
                    link5 = kr_link5, link6 = kr_link6,
                    link7 = kr_link7, link8 = kr_link8,
                    link9 = kr_link9, link10 = kr_link10)

    df_NA = scrape_na(link1 = na_link1, link2 = na_link2, 
                    link3 = na_link3, link4 = na_link4, 
                    link5 = na_link5, link6 = na_link6,
                    link7 = na_link7, link8 = na_link8,
                    link9 = na_link9, link10 = na_link10)

    df_EU = scrape_eu(link1 = eu_link1, link2 = eu_link2, 
                    link3 = eu_link3, link4 = eu_link4, 
                    link5 = eu_link5, link6 = eu_link6,
                    link7 = eu_link7, link8 = eu_link8,
                    link9 = eu_link9, link10 = eu_link10)

    df_BR = scrape_br(link1 = br_link1, link2 = br_link2, 
                    link3 = br_link3, link4 = br_link4, 
                    link5 = br_link5, link6 = br_link6,
                    link7 = br_link7, link8 = br_link8,
                    link9 = br_link9, link10 = br_link10)

    df_LA = scrape_la(link1 = la_link1, link2 = la_link2, 
                    link3 = la_link3, link4 = la_link4, 
                    link5 = la_link5, link6 = la_link6,
                    link7 = la_link7, link8 = la_link8,
                    link9 = la_link9, link10 = la_link10)

    df_AP = scrape_ap(link1 = ap_link1, link2 = ap_link2, 
                    link3 = ap_link3, link4 = ap_link4, 
                    link5 = ap_link5, link6 = ap_link6,
                    link7 = ap_link7, link8 = ap_link8,
                    link9 = ap_link9, link10 = ap_link10)


    # concat df created from scraping functions
    df_combined = pd.concat([df_NA, 
                          df_EU,
                          df_KR, 
                          df_BR, 
                          df_LA, 
                          df_AP])

    df_final = wrangle(df_combined)

    table.insert(dict(
                        Rank=df_final['Rank'],
                        Player=df_final['Player'],
                        Rating=df_final['Rating'],
                        Winrate=df_final['Winrate'],
                        Games=df_final['Games'],
                        Average_Score=df_final['Average_Score'],
                        Head_Shot_Pct=df_final['Head_Shot_Pct'],
                        Class=df_final['Class'],
                        Region=df_final['Region'],
                        ))

    curs.close()
    conn.close()


def scrape(link):
    '''
    scrape Valorant stats from the Top 500 players in 
    (NA, Korea, EU, Asian Pacific, BR, LATAT)
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


'''
The below functions are scraping functions for individual regions
Korea, Europe, North America, Latin America, Brazil, Asia Pacific
'''

def scrape_kr(link1 = dak_links.kr_link1, link2 = dak_links.kr_link2, 
               link3 = dak_links.kr_link3, link4 = dak_links.kr_link4, 
               link5 = dak_links.kr_link5, link6 = dak_links.kr_link6,
               link7 = dak_links.kr_link7, link8 = dak_links.kr_link8,
               link9 = dak_links.kr_link9, link10 = dak_links.kr_link10):
    '''
    Create Top 500 Korean df's based off of dak_links py file
    '''
    df_kr1 = scrape(link1)
    df_kr2 = scrape(link2)
    df_kr3 = scrape(link3)
    df_kr4 = scrape(link4)
    df_kr5 = scrape(link5)
    df_kr6 = scrape(link6)
    df_kr7 = scrape(link7)
    df_kr8 = scrape(link8)
    df_kr9 = scrape(link9)
    df_kr10 = scrape(link10)

    #Concatenate the Top 500 Korean dataframe
    df_KR = pd.concat([df_kr1, 
       df_kr2,
       df_kr3, 
       df_kr4, 
       df_kr5, 
       df_kr6, 
       df_kr7, 
       df_kr8, 
       df_kr9, 
       df_kr10])

    #Add Region feature dataframe
    df_KR['Region'] = 'Korea'

    #Drop Most Agent Columns
    df_KR.drop(columns= 'Most Agents', inplace=True)

    return df_KR


def scrape_eu(link1 = dak_links.eu_link1, link2 = dak_links.eu_link2, 
              link3 = dak_links.eu_link3, link4 = dak_links.eu_link4, 
              link5 = dak_links.eu_link5, link6 = dak_links.eu_link6,
              link7 = dak_links.eu_link7, link8 = dak_links.eu_link8,
              link9 = dak_links.eu_link9, link10 = dak_links.eu_link10):
    '''
    Create Top 500 EU df's based off of dak_links py file
    '''
    df_eu1 = scrape(link1)
    df_eu2 = scrape(link2)
    df_eu3 = scrape(link3)
    df_eu4 = scrape(link4)
    df_eu5 = scrape(link5)
    df_eu6 = scrape(link6)
    df_eu7 = scrape(link7)
    df_eu8 = scrape(link8)
    df_eu9 = scrape(link9)
    df_eu10 = scrape(link10)

    #Concatenate the Top 500 European dataframe
    df_EU = pd.concat([df_eu1, 
                     df_eu2,
                     df_eu3, 
                     df_eu4, 
                     df_eu5, 
                     df_eu6, 
                     df_eu7, 
                     df_eu8, 
                     df_eu9, 
                     df_eu10])
                     
    #Add Region feature dataframe
    df_EU['Region'] = 'Europe'

    #Drop Most Agent Columns
    df_EU.drop(columns= 'Most Agents', inplace=True)

    return df_EU


def scrape_na(link1 = dak_links.na_link1, link2 = dak_links.na_link2, 
              link3 = dak_links.na_link3, link4 = dak_links.na_link4, 
              link5 = dak_links.na_link5, link6 = dak_links.na_link6,
              link7 = dak_links.na_link7, link8 = dak_links.na_link8,
              link9 = dak_links.na_link9, link10 = dak_links.na_link10):
    '''
    Create Top 500 NA df's based off of dak_links py file
    '''
    df_na1 = scrape(link1)
    df_na2 = scrape(link2)
    df_na3 = scrape(link3)
    df_na4 = scrape(link4)
    df_na5 = scrape(link5)
    df_na6 = scrape(link6)
    df_na7 = scrape(link7)
    df_na8 = scrape(link8)
    df_na9 = scrape(link9)
    df_na10 = scrape(link10)

    #Concatenate the Top 500 NA dataframe
    df_NA = pd.concat([df_na1, 
                   df_na2,
                   df_na3, 
                   df_na4, 
                   df_na5, 
                   df_na6, 
                   df_na7, 
                   df_na8, 
                   df_na9, 
                   df_na10])

    #Add Region feature dataframe
    df_NA['Region'] = 'North America'

    #Drop Most Agent Columns
    df_NA.drop(columns= 'Most Agents', inplace=True)

    return df_NA


def scrape_ap(link1 = dak_links.ap_link1, link2 = dak_links.ap_link2, 
              link3 = dak_links.ap_link3, link4 = dak_links.ap_link4, 
              link5 = dak_links.ap_link5, link6 = dak_links.ap_link6,
              link7 = dak_links.ap_link7, link8 = dak_links.ap_link8,
              link9 = dak_links.ap_link9, link10 = dak_links.ap_link10):
    '''
    Create Top 500 Asia Pacific df's based off of dak_links py file
    '''
    df_ap1 = scrape(link1)
    df_ap2 = scrape(link2)
    df_ap3 = scrape(link3)
    df_ap4 = scrape(link4)
    df_ap5 = scrape(link5)
    df_ap6 = scrape(link6)
    df_ap7 = scrape(link7)
    df_ap8 = scrape(link8)
    df_ap9 = scrape(link9)
    df_ap10 = scrape(link10)

    #Concatenate the Top 500 AP dataframe
    df_AP = pd.concat([df_ap1, 
                   df_ap2,
                   df_ap3, 
                   df_ap4, 
                   df_ap5, 
                   df_ap6, 
                   df_ap7, 
                   df_ap8, 
                   df_ap9, 
                   df_ap10])

    #Add Region feature dataframe
    df_AP['Region'] = 'Asia Pacific'

    #Drop Most Agent Columns
    df_AP.drop(columns= 'Most Agents', inplace=True)

    return df_AP


def scrape_br(link1 = dak_links.br_link1, link2 = dak_links.br_link2, 
              link3 = dak_links.br_link3, link4 = dak_links.br_link4, 
              link5 = dak_links.br_link5, link6 = dak_links.br_link6,
              link7 = dak_links.br_link7, link8 = dak_links.br_link8,
              link9 = dak_links.br_link9, link10 = dak_links.br_link10):
    '''
    Create Top 500 Brazil df's based off of dak_links py file
    '''
    df_br1 = scrape(link1)
    df_br2 = scrape(link2)
    df_br3 = scrape(link3)
    df_br4 = scrape(link4)
    df_br5 = scrape(link5)
    df_br6 = scrape(link6)
    df_br7 = scrape(link7)
    df_br8 = scrape(link8)
    df_br9 = scrape(link9)
    df_br10 = scrape(link10)

    #Concatenate the Top 500 BR dataframe
    df_BR = pd.concat([df_br1, 
                   df_br2,
                   df_br3, 
                   df_br4, 
                   df_br5, 
                   df_br6, 
                   df_br7, 
                   df_br8, 
                   df_br9, 
                   df_br10])

    #Add Region feature dataframe
    df_BR['Region'] = 'Brazil'

    #Drop Most Agent Columns
    df_BR.drop(columns= 'Most Agents', inplace=True)

    return df_BR


def scrape_la(link1 = dak_links.la_link1, link2 = dak_links.la_link2, 
              link3 = dak_links.la_link3, link4 = dak_links.la_link4, 
              link5 = dak_links.la_link5, link6 = dak_links.la_link6,
              link7 = dak_links.la_link7, link8 = dak_links.la_link8,
              link9 = dak_links.la_link9, link10 = dak_links.la_link10):
    '''
    Create Top 500 Latin America df's based off of dak_links py file
    '''
    df_la1 = scrape(link1)
    df_la2 = scrape(link2)
    df_la3 = scrape(link3)
    df_la4 = scrape(link4)
    df_la5 = scrape(link5)
    df_la6 = scrape(link6)
    df_la7 = scrape(link7)
    df_la8 = scrape(link8)
    df_la9 = scrape(link9)
    df_la10 = scrape(link10)

    #Concatenate the Top 500 LATAM dataframe
    df_LA = pd.concat([df_la1, 
                   df_la2,
                   df_la3, 
                   df_la4, 
                   df_la5, 
                   df_la6, 
                   df_la7, 
                   df_la8, 
                   df_la9, 
                   df_la10])

    #Add Region feature dataframe
    df_LA['Region'] = 'Latin America'

    #Drop Most Agent Columns
    df_LA.drop(columns= 'Most Agents', inplace=True)

    return df_LA
