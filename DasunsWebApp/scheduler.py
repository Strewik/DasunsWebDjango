import scheduler
import time
import requests
url = ''
page = requests.get(url)
data = page.json()


def fetch_somedata():
    print('getting the data...')
    results = data #[some args]
    print('results')

def job():
    print("Reading time...")
    
def coding():
    print("Coding time...")
    
def playing():
    print("Playing time...")
    
#Time 
schedule.every(10).seconds.do(job)
schedule.every(5).seconds.do(coding)
schedule.every(5).seconds.do(fetch_somedata)
schedule.every().day.at("12:00").do(playing)

while True:
    schedule.run_pending()
    time.sleep(1)