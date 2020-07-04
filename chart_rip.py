import requests
from bs4 import BeautifulSoup

def get_week(url):
    '''
    Gets the billboard.com chart residing in the given url.
    '''

    response = requests.get(url) # http request for the page
    soup = BeautifulSoup(response.text, "html.parser") # scrape the page

    container = soup.find_all(id = 'charts') # get the html of the chart container
    
    date = container[0]['data-chart-date'] # date of the chart
    code = container[0]['data-chart-title'] # name of the chart

    rows = soup.find_all(class_ = 'chart-element__wrapper') # get all the chart items
    dict = {'date': date, 'code': code, 'chartRows': []}    # stores the scrapped chart info
    
    for row in rows: # for all songs
         position = row.find(class_='chart-element__rank__number').string       # get the position
         artist = row.find(class_='chart-element__information__artist').string  # get the artist
         title = row.find(class_='chart-element__information__song').string     # get the song title
         trend = row.find(class_='chart-element__trend').string                 # get the song's trend

         meta = row.find_all(class_='chart-element__meta')
         
         lastWeek = meta[0].string  # get the song's last week position
         peak = meta[1].string      # get the song's peak
         duration = meta[2].string  # get the song's number of weeks on the chart

         # add the song
         dict['chartRows'].append({'tw': position, 'lw': lastWeek, 'title': title, "artist": artist, 'peak': peak, 'wc': duration, 'trend': trend})
   
    return dict
