import requests
from bs4 import BeautifulSoup
import pandas


url = 'https://www.accuweather.com/en/ro/targu-jiu/273335/hourly-weather-forecast/erwsersersreersresersre'
my_headers={"User-Agent":"Mozilla/5.0"}
page=requests.get(url,headers=my_headers)
soup=BeautifulSoup(page.content,'html.parser')

a = soup.find(class_='hourly-wrapper content-module')

b=a.find_all(class_='accordion-item hourly-card-nfl hour non-ad')

time=soup.find_all(class_='hourly-card-nfl-header')
print(time[0].find('span').text)
print(time[0].find(class_='temp metric').get_text(strip=True))
print(time[0].find(class_='phrase').get_text(strip=True))
print(time[0].find(class_='precip').get_text(strip=True))

time_clock = [timee.find('span').get_text(strip=True) for timee in time]
temp_metric= [timee.find(class_='temp metric').get_text(strip=True) for timee in time]
phrase= [timee.find(class_='phrase').get_text(strip=True) for timee in time]
precip= [timee.find(class_='precip').get_text(strip=True) for timee in time]
print(time_clock)

print(temp_metric)

print(phrase)

print(precip)

vremea = pandas.DataFrame({'Ora': time_clock,
                           'Temperatura': temp_metric,
                           'Stare': phrase,
                           'Precipitatii': precip})




print(vremea)

vremea.to_csv('your22.csv', index=False)