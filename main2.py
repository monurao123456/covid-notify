from msilib.schema import Icon
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notifyme(title, message):
    notification.notify (
  title= title, 
  message=message,
  app_icon="icon.ico",
  timeout=3,)

def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    notifyme("rampal","notification")
    myHtmlData = getData('https://www.mohfw.gov.in')
    
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())
    for link in soup.find_all('ul')[48]:
        print(link.get_text())
