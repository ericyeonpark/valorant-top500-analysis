import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import dak_links

def scrape(link):
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


def scrape_kor(link1 = dak_links.kr_link1, link2 = dak_links.kr_link2, 
               link3 = dak_links.kr_link3, link4 = dak_links.kr_link4, 
               link5 = dak_links.kr_link5, link6 = dak_links.kr_link6,
               link7 = dak_links.kr_link7, link8 = dak_links.kr_link8,
               link9 = dak_links.kr_link9, link10 = dak_links.kr_link10):
    '''
    Create Top 500 Korean df's based off of dak_links py file
    '''
    df_kr1 = scrape(link1)
    print('worked')
    df_kr2 = scrape(link2)
    df_kr3 = scrape(link3)
    df_kr4 = scrape(link4)
    df_kr5 = scrape(link5)
    df_kr6 = scrape(link6)
    df_kr7 = scrape(link7)
    df_kr8 = scrape(link8)
    df_kr9 = scrape(link9)
    df_kr10 = scrape(link10)

    return df_kr1, df_kr2, df_kr3, df_kr4, df_kr5, \
           df_kr6, df_kr7, df_kr8, df_kr9, df_kr10


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

    return df_eu1, df_eu2, df_eu3, df_eu4, df_eu5, \
           df_eu6, df_eu7, df_eu8, df_eu9, df_eu10


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

    return df_na1, df_na2, df_na3, df_na4, df_na5, \
           df_na6, df_na7, df_na8, df_na9, df_na10


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

    return df_ap1, df_ap2, df_ap3, df_ap4, df_ap5, \
           df_ap6, df_ap7, df_ap8, df_ap9, df_ap10


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

    return df_br1, df_br2, df_br3, df_br4, df_br5, \
           df_br6, df_br7, df_br8, df_br9, df_br10


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

    return df_la1, df_la2, df_la3, df_la4, df_la5, \
           df_la6, df_la7, df_la8, df_la9, df_la10
