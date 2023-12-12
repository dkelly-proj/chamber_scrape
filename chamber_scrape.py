# Imports
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Chamber Events
## Worthington
url = 'https://business.worthingtonchamber.org/calendar'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

worthington_events = []

try:
    for item in soup.find_all('div', class_="card-body gz-events-card-body"):
        chamber = 'Worthington'
        sdate = pd.to_datetime(str(item).split('meta content')[1].split('"')[1].split(' ')[0]).date()
        
        try:
            stime = str(item).split('gz-event-card-time">')[1].split('<')[0]
        except:
            stime = None
    
        event = str(item).split('itemprop="url">')[1].split('<')[0]
            
        worthington_events.append({'Chamber': chamber, 'Date': sdate, 'Time': stime, 'Event': event})

except:
    worthington_events.append({'Chamber': 'Error', 'Date': 'Error', 'Time': 'Error', 'Event': 'Error'})

## Dublin
url = 'https://www.dublinchamber.org/events/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

dublin_events = []

try:
    for item in soup.find_all('div', class_="card-body gz-events-card-title"):
        chamber = 'Dublin'
        sdate = pd.to_datetime(str(item).split('span content="')[1].split('T')[0]).date()
        stime = None
        event = str(item).split('gz-card-title"')[1].split('">')[1].split('<')[0]
    
        dublin_events.append({'Chamber': chamber, 'Date': sdate, 'Time': stime, 'Event': event})

except:
    dublin_events.append({'Chamber': 'Error', 'Date': 'Error', 'Time': 'Error', 'Event': 'Error'})

## Tri-Village
url = 'https://business.chamberpartnership.org/events'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

tv_events = []

try:
    for item in soup.find_all('div', class_='mn-listingcontent'):
        chamber = 'Tri-Village'
        sdate = pd.to_datetime(str(item).split('span content="')[1].split('T')[0]).date()
        stime = pd.to_datetime(str(item).split('span content="')[1].split('T')[1].split('"')[0]).time()
        event = str(item).split('itemprop="url">')[1].split('<')[0]
    
        tv_events.append({'Chamber': chamber, 'Date': sdate, 'Time': stime, 'Event': event})

except:
    tv_events.append({'Chamber': 'Error', 'Date': 'Error', 'Time': 'Error', 'Event': 'Error'})

## Hilliard
url = 'https://business.hilliardchamber.org/events'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

hilliard_events = []

try:
    for item in soup.find_all('div', class_='card-body gz-events-card-title'):
        chamber = 'Hilliard'
        sdate = pd.to_datetime(str(item).split('span content="')[1].split('T')[0]).date()
        stime = pd.to_datetime(str(item).split('span content="')[1].split('T')[1].split('"')[0]).time()
        event = str(item).split('<a href="')[1].split('">')[1].split('</a')[0]
    
        hilliard_events.append({'Chamber': chamber, 'Date': sdate, 'Time': stime, 'Event': event})

except:
    hilliard_events.append({'Chamber': 'Error', 'Date': 'Error', 'Time': 'Error', 'Event': 'Error'})

# Combine
(pd.concat([pd.DataFrame(worthington_events), 
            pd.DataFrame(dublin_events),
            pd.DataFrame(tv_events),
            pd.DataFrame(hilliard_events)])
     .sort_values('Date')
     .to_csv('Chamber_Events.csv', index = False))













