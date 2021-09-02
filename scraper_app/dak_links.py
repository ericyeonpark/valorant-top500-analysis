'''
Python file storing scraped links for the latest season
'''
def create_link_kr():
    '''
    create links to scrape for kr server. Will find the links from the latest act and season
    '''
    for season in range(2, 10, 1):
        for act in range(1, 4, 1):
            kr_link1 = 'https://dak.gg/valorant/leaderboard?season={}&act={}&shard=kr'.format(season, act)
            kr_link2 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=2&season={}&act={}'.format(season, act)
            kr_link3 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=3&season={}&act={}'.format(season, act)
            kr_link4 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=4&season={}&act={}'.format(season, act)
            kr_link5 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=5&season={}&act={}'.format(season, act)
            kr_link6 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=6&season={}&act={}'.format(season, act)
            kr_link7 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=7&season={}&act={}'.format(season, act)
            kr_link8 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=8&season={}&act={}'.format(season, act)
            kr_link9 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=9&season={}&act={}'.format(season, act)
            kr_link10 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=10&season={}&act={}'.format(season, act)
            try:
                scrape(kr_link10)

            except IndexError:
                print('Latest Error Season: ', season, 'Latest Error Act: ', act) 
                # you can intuitively see what the latest season and act is from the 1st print statement
                # i.e. if printed Act = 4 then Act = 3, printed Act = 2 then Act = 1
                # i.e  if printed Act = 1, then Act = 3 AND Season = -1 since it's one season back
                kr_link1 = 'https://dak.gg/valorant/leaderboard?season={}&act={}&shard=kr'.format(season, act-1)
                kr_link2 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=2&season={}&act={}'.format(season, act-1)
                kr_link3 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=3&season={}&act={}'.format(season, act-1)
                kr_link4 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=4&season={}&act={}'.format(season, act-1)
                kr_link5 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=5&season={}&act={}'.format(season, act-1)
                kr_link6 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=6&season={}&act={}'.format(season, act-1)
                kr_link7 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=7&season={}&act={}'.format(season, act-1)
                kr_link8 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=8&season={}&act={}'.format(season, act-1)
                kr_link9 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=9&season={}&act={}'.format(season, act-1)
                kr_link10 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=10&season={}&act={}'.format(season, act-1)
                break

    return kr_link1, kr_link2, kr_link3, kr_link4, kr_link5, \
        kr_link6, kr_link7, kr_link8, kr_link9, kr_link10


def create_link_eu():
    '''
    create links to scrape for eu server. Will find the links from the latest act and season
    '''
    for season in range(2, 10, 1):
        for act in range(1, 4, 1):
            eu_link1 = 'https://dak.gg/valorant/leaderboard?season={}&act={}&shard=eu'.format(season, act)
            eu_link2 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=2&season={}&act={}'.format(season, act)
            eu_link3 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=3&season={}&act={}'.format(season, act)
            eu_link4 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=4&season={}&act={}'.format(season, act)
            eu_link5 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=5&season={}&act={}'.format(season, act)
            eu_link6 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=6&season={}&act={}'.format(season, act)
            eu_link7 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=7&season={}&act={}'.format(season, act)
            eu_link8 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=8&season={}&act={}'.format(season, act)
            eu_link9 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=9&season={}&act={}'.format(season, act)
            eu_link10 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=10&season={}&act={}'.format(season, act)
            try:
                scrape(eu_link10)

            except IndexError:
                print('Latest Error Season: ', season, 'Latest Error Act: ', act) 
                # you can intuitively see what the latest season and act is from the 1st print statement
                # i.e. if printed Act = 4 then Act = 3, printed Act = 2 then Act = 1
                # i.e  if printed Act = 1, then Act = 3 AND Season = -1 since it's one season back
                eu_link1 = 'https://dak.gg/valorant/leaderboard?season={}&act={}&shard=eu'.format(season, act-1)
                eu_link2 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=2&season={}&act={}'.format(season, act-1)
                eu_link3 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=3&season={}&act={}'.format(season, act-1)
                eu_link4 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=4&season={}&act={}'.format(season, act-1)
                eu_link5 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=5&season={}&act={}'.format(season, act-1)
                eu_link6 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=6&season={}&act={}'.format(season, act-1)
                eu_link7 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=7&season={}&act={}'.format(season, act-1)
                eu_link8 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=8&season={}&act={}'.format(season, act-1)
                eu_link9 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=9&season={}&act={}'.format(season, act-1)
                eu_link10 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=10&season={}&act={}'.format(season, act-1)
                break

    return eu_link1, eu_link2, eu_link3, eu_link4, eu_link5, \
        eu_link6, eu_link7, eu_link8, eu_link9, eu_link10


def create_link_na():
    '''
    create links to scrape for na server. Will find the links from the latest act and season
    '''
    for season in range(2, 10, 1):
        for act in range(1, 4, 1):
            na_link1 = 'https://dak.gg/valorant/leaderboard?season={}&act={}&shard=na'.format(season, act)
            na_link2 = 'https://dak.gg/valorant/leaderboard?shard=na&page=2&season={}&act={}'.format(season, act)
            na_link3 = 'https://dak.gg/valorant/leaderboard?shard=na&page=3&season={}&act={}'.format(season, act)
            na_link4 = 'https://dak.gg/valorant/leaderboard?shard=na&page=4&season={}&act={}'.format(season, act)
            na_link5 = 'https://dak.gg/valorant/leaderboard?shard=na&page=5&season={}&act={}'.format(season, act)
            na_link6 = 'https://dak.gg/valorant/leaderboard?shard=na&page=6&season={}&act={}'.format(season, act)
            na_link7 = 'https://dak.gg/valorant/leaderboard?shard=na&page=7&season={}&act={}'.format(season, act)
            na_link8 = 'https://dak.gg/valorant/leaderboard?shard=na&page=8&season={}&act={}'.format(season, act)
            na_link9 = 'https://dak.gg/valorant/leaderboard?shard=na&page=9&season={}&act={}'.format(season, act)
            na_link10 = 'https://dak.gg/valorant/leaderboard?shard=na&page=10&season={}&act={}'.format(season, act)
            try:
                scrape(na_link10)

            except IndexError:
                print('Latest Error Season: ', season, 'Latest Error Act: ', act) 
                # you can intuitively see what the latest season and act is from the 1st print statement
                # i.e. if printed Act = 4 then Act = 3, printed Act = 2 then Act = 1
                # i.e  if printed Act = 1, then Act = 3 AND Season = -1 since it's one season back
                na_link1 = 'https://dak.gg/valorant/leaderboard?season={}&act={}&shard=na'.format(season, act-1)
                na_link2 = 'https://dak.gg/valorant/leaderboard?shard=na&page=2&season={}&act={}'.format(season, act-1)
                na_link3 = 'https://dak.gg/valorant/leaderboard?shard=na&page=3&season={}&act={}'.format(season, act-1)
                na_link4 = 'https://dak.gg/valorant/leaderboard?shard=na&page=4&season={}&act={}'.format(season, act-1)
                na_link5 = 'https://dak.gg/valorant/leaderboard?shard=na&page=5&season={}&act={}'.format(season, act-1)
                na_link6 = 'https://dak.gg/valorant/leaderboard?shard=na&page=6&season={}&act={}'.format(season, act-1)
                na_link7 = 'https://dak.gg/valorant/leaderboard?shard=na&page=7&season={}&act={}'.format(season, act-1)
                na_link8 = 'https://dak.gg/valorant/leaderboard?shard=na&page=8&season={}&act={}'.format(season, act-1)
                na_link9 = 'https://dak.gg/valorant/leaderboard?shard=na&page=9&season={}&act={}'.format(season, act-1)
                na_link10 = 'https://dak.gg/valorant/leaderboard?shard=na&page=10&season={}&act={}'.format(season, act-1)
                break

    return na_link1, na_link2, na_link3, na_link4, na_link5, \
        na_link6, na_link7, na_link8, na_link9, na_link10


def create_link_ap():
    '''
    create links to scrape for ap server. Will find the links from the latest act and season
    '''
    for season in range(2, 10, 1):
        for act in range(1, 4, 1):
            ap_link1 = 'https://dak.gg/valorant/leaderboard?season={}&act={}&shard=ap'.format(season, act)
            ap_link2 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=2&season={}&act={}'.format(season, act)
            ap_link3 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=3&season={}&act={}'.format(season, act)
            ap_link4 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=4&season={}&act={}'.format(season, act)
            ap_link5 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=5&season={}&act={}'.format(season, act)
            ap_link6 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=6&season={}&act={}'.format(season, act)
            ap_link7 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=7&season={}&act={}'.format(season, act)
            ap_link8 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=8&season={}&act={}'.format(season, act)
            ap_link9 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=9&season={}&act={}'.format(season, act)
            ap_link10 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=10&season={}&act={}'.format(season, act)
            try:
                scrape(ap_link10)

            except IndexError:
                print('Latest Error Season: ', season, 'Latest Error Act: ', act) 
                # you can intuitively see what the latest season and act is from the 1st print statement
                # i.e. if printed Act = 4 then Act = 3, printed Act = 2 then Act = 1
                # i.e  if printed Act = 1, then Act = 3 AND Season = -1 since it's one season back
                ap_link1 = 'https://dak.gg/valorant/leaderboard?season={}&act={}&shard=ap'.format(season, act-1)
                ap_link2 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=2&season={}&act={}'.format(season, act-1)
                ap_link3 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=3&season={}&act={}'.format(season, act-1)
                ap_link4 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=4&season={}&act={}'.format(season, act-1)
                ap_link5 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=5&season={}&act={}'.format(season, act-1)
                ap_link6 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=6&season={}&act={}'.format(season, act-1)
                ap_link7 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=7&season={}&act={}'.format(season, act-1)
                ap_link8 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=8&season={}&act={}'.format(season, act-1)
                ap_link9 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=9&season={}&act={}'.format(season, act-1)
                ap_link10 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=10&season={}&act={}'.format(season, act-1)
                break


    return ap_link1, ap_link2, ap_link3, ap_link4, ap_link5, \
        ap_link6, ap_link7, ap_link8, ap_link9, ap_link10


def create_link_br():
    '''
    create links to scrbre for br server. Will find the links from the latest act and season
    '''
    for season in range(2, 10, 1):
        for act in range(1, 4, 1):
            br_link1 = 'https://dak.gg/valorant/leaderboard?season={}&act={}&shard=br'.format(season, act)
            br_link2 = 'https://dak.gg/valorant/leaderboard?shard=br&page=2&season={}&act={}'.format(season, act)
            br_link3 = 'https://dak.gg/valorant/leaderboard?shard=br&page=3&season={}&act={}'.format(season, act)
            br_link4 = 'https://dak.gg/valorant/leaderboard?shard=br&page=4&season={}&act={}'.format(season, act)
            br_link5 = 'https://dak.gg/valorant/leaderboard?shard=br&page=5&season={}&act={}'.format(season, act)
            br_link6 = 'https://dak.gg/valorant/leaderboard?shard=br&page=6&season={}&act={}'.format(season, act)
            br_link7 = 'https://dak.gg/valorant/leaderboard?shard=br&page=7&season={}&act={}'.format(season, act)
            br_link8 = 'https://dak.gg/valorant/leaderboard?shard=br&page=8&season={}&act={}'.format(season, act)
            br_link9 = 'https://dak.gg/valorant/leaderboard?shard=br&page=9&season={}&act={}'.format(season, act)
            br_link10 = 'https://dak.gg/valorant/leaderboard?shard=br&page=10&season={}&act={}'.format(season, act)
            try:
                scrape(br_link10)

            except IndexError:
                print('Latest Error Season: ', season, 'Latest Error Act: ', act) 
                # you can intuitively see what the latest season and act is from the 1st print statement
                # i.e. if printed Act = 4 then Act = 3, printed Act = 2 then Act = 1
                # i.e  if printed Act = 1, then Act = 3 AND Season = -1 since it's one season back
                br_link1 = 'https://dak.gg/valorant/leaderboard?season={}&act={}&shard=br'.format(season, act-1)
                br_link2 = 'https://dak.gg/valorant/leaderboard?shard=br&page=2&season={}&act={}'.format(season, act-1)
                br_link3 = 'https://dak.gg/valorant/leaderboard?shard=br&page=3&season={}&act={}'.format(season, act-1)
                br_link4 = 'https://dak.gg/valorant/leaderboard?shard=br&page=4&season={}&act={}'.format(season, act-1)
                br_link5 = 'https://dak.gg/valorant/leaderboard?shard=br&page=5&season={}&act={}'.format(season, act-1)
                br_link6 = 'https://dak.gg/valorant/leaderboard?shard=br&page=6&season={}&act={}'.format(season, act-1)
                br_link7 = 'https://dak.gg/valorant/leaderboard?shard=br&page=7&season={}&act={}'.format(season, act-1)
                br_link8 = 'https://dak.gg/valorant/leaderboard?shard=br&page=8&season={}&act={}'.format(season, act-1)
                br_link9 = 'https://dak.gg/valorant/leaderboard?shard=br&page=9&season={}&act={}'.format(season, act-1)
                br_link10 = 'https://dak.gg/valorant/leaderboard?shard=br&page=10&season={}&act={}'.format(season, act-1)
                break


    return br_link1, br_link2, br_link3, br_link4, br_link5, \
        br_link6, br_link7, br_link8, br_link9, br_link10


def create_link_la():
    '''
    create links to scrape for la server. Will find the links from the latest act and season
    '''
    for season in range(2, 10, 1):
        for act in range(1, 4, 1):
            la_link1 = 'https://dak.gg/valorant/leaderboard?season={}&act={}&shard=latam'.format(season, act)
            la_link2 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=2&season={}&act={}'.format(season, act)
            la_link3 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=3&season={}&act={}'.format(season, act)
            la_link4 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=4&season={}&act={}'.format(season, act)
            la_link5 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=5&season={}&act={}'.format(season, act)
            la_link6 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=6&season={}&act={}'.format(season, act)
            la_link7 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=7&season={}&act={}'.format(season, act)
            la_link8 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=8&season={}&act={}'.format(season, act)
            la_link9 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=9&season={}&act={}'.format(season, act)
            la_link10 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=10&season={}&act={}'.format(season, act)
            try:
                scrape(la_link10)

            except IndexError:
                print('Latest Error Season: ', season, 'Latest Error Act: ', act) 
                # you can intuitively see what the latest season and act is from the 1st print statement
                # i.e. if printed Act = 4 then Act = 3, printed Act = 2 then Act = 1
                # i.e  if printed Act = 1, then Act = 3 AND Season = -1 since it's one season back
                la_link1 = 'https://dak.gg/valorant/leaderboard?season={}&act={}&shard=latam'.format(season, act-1)
                la_link2 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=2&season={}&act={}'.format(season, act-1)
                la_link3 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=3&season={}&act={}'.format(season, act-1)
                la_link4 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=4&season={}&act={}'.format(season, act-1)
                la_link5 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=5&season={}&act={}'.format(season, act-1)
                la_link6 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=6&season={}&act={}'.format(season, act-1)
                la_link7 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=7&season={}&act={}'.format(season, act-1)
                la_link8 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=8&season={}&act={}'.format(season, act-1)
                la_link9 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=9&season={}&act={}'.format(season, act-1)
                la_link10 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=10&season={}&act={}'.format(season, act-1)
                break


    return la_link1, la_link2, la_link3, la_link4, la_link5, \
        la_link6, la_link7, la_link8, la_link9, la_link10
        
                
# OLD CODE. MAYBE SHOULD DELETE           

# #Create Top 500 Korean stat links 
# kr_link1 = 'https://dak.gg/valorant/leaderboard'
# kr_link2 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=2&season=2&act=2'
# kr_link3 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=3&season=2&act=2'
# kr_link4 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=4&season=2&act=2'
# kr_link5 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=5&season=2&act=2'
# kr_link6 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=6&season=2&act=2'
# kr_link7 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=7&season=2&act=2'
# kr_link8 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=8&season=2&act=2'
# kr_link9 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=9&season=2&act=2'
# kr_link10 = 'https://dak.gg/valorant/leaderboard?shard=kr&page=10&season=2&act=2'


# #Create Top 500 European stat links
# eu_link1 = 'https://dak.gg/valorant/leaderboard?shard=eu'
# eu_link2 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=2&season=2&act=2'
# eu_link3 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=3&season=2&act=2'
# eu_link4 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=4&season=2&act=2'
# eu_link5 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=5&season=2&act=2'
# eu_link6 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=6&season=2&act=2'
# eu_link7 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=7&season=2&act=2'
# eu_link8 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=8&season=2&act=2'
# eu_link9 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=9&season=2&act=2'
# eu_link10 = 'https://dak.gg/valorant/leaderboard?shard=eu&page=10&season=2&act=2'


# #Create Top 500 NA stat links
# na_link1 = 'https://dak.gg/valorant/leaderboard?shard=na'
# na_link2 = 'https://dak.gg/valorant/leaderboard?shard=na&page=2&season=2&act=2'
# na_link3 = 'https://dak.gg/valorant/leaderboard?shard=na&page=3&season=2&act=2'
# na_link4 = 'https://dak.gg/valorant/leaderboard?shard=na&page=4&season=2&act=2'
# na_link5 = 'https://dak.gg/valorant/leaderboard?shard=na&page=5&season=2&act=2'
# na_link6 = 'https://dak.gg/valorant/leaderboard?shard=na&page=6&season=2&act=2'
# na_link7 = 'https://dak.gg/valorant/leaderboard?shard=na&page=7&season=2&act=2'
# na_link8 = 'https://dak.gg/valorant/leaderboard?shard=na&page=8&season=2&act=2'
# na_link9 = 'https://dak.gg/valorant/leaderboard?shard=na&page=9&season=2&act=2'
# na_link10 = 'https://dak.gg/valorant/leaderboard?shard=na&page=10&season=2&act=2'


# #Create Top 500 AP stat links
# ap_link1 = 'https://dak.gg/valorant/leaderboard?shard=ap'
# ap_link2 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=2&season=2&act=2'
# ap_link3 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=3&season=2&act=2'
# ap_link4 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=4&season=2&act=2'
# ap_link5 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=5&season=2&act=2'
# ap_link6 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=6&season=2&act=2'
# ap_link7 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=7&season=2&act=2'
# ap_link8 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=8&season=2&act=2'
# ap_link9 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=9&season=2&act=2'
# ap_link10 = 'https://dak.gg/valorant/leaderboard?shard=ap&page=10&season=2&act=2'


# #Create Top 500 BR stat links
# br_link1 = 'https://dak.gg/valorant/leaderboard?shard=br'
# br_link2 = 'https://dak.gg/valorant/leaderboard?shard=br&page=2&season=2&act=2'
# br_link3 = 'https://dak.gg/valorant/leaderboard?shard=br&page=3&season=2&act=2'
# br_link4 = 'https://dak.gg/valorant/leaderboard?shard=br&page=4&season=2&act=2'
# br_link5 = 'https://dak.gg/valorant/leaderboard?shard=br&page=5&season=2&act=2'
# br_link6 = 'https://dak.gg/valorant/leaderboard?shard=br&page=6&season=2&act=2'
# br_link7 = 'https://dak.gg/valorant/leaderboard?shard=br&page=7&season=2&act=2'
# br_link8 = 'https://dak.gg/valorant/leaderboard?shard=br&page=8&season=2&act=2'
# br_link9 = 'https://dak.gg/valorant/leaderboard?shard=br&page=9&season=2&act=2'
# br_link10 = 'https://dak.gg/valorant/leaderboard?shard=br&page=10&season=2&act=2'


# #Create Top 500 LATAM stat links
# la_link1 = 'https://dak.gg/valorant/leaderboard?shard=latam'
# la_link2 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=2&season=2&act=2'
# la_link3 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=3&season=2&act=2'
# la_link4 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=4&season=2&act=2'
# la_link5 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=5&season=2&act=2'
# la_link6 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=6&season=2&act=2'
# la_link7 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=7&season=2&act=2'
# la_link8 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=8&season=2&act=2'
# la_link9 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=9&season=2&act=2'
# la_link10 = 'https://dak.gg/valorant/leaderboard?shard=latam&page=10&season=2&act=2'