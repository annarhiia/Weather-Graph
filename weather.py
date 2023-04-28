import matplotlib.pyplot as plt
import numpy as np
import requests
import pygame
import weatherdisplay
import weather

city = input("please type a city:")


def graph():
    x1 = [17, 18, 19, 20, 21]
    y1 = [3.4, 4.2, 3.4, 6.8, 11]

    plt.plot(x1, y1, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)

    TOKEN = "d96ef914f824ea366cdbdc0c15032233"
    token = "e417573a625de57e47c56ad00f863d9c"

    url1 = 'http://api.positionstack.com/v1/forward?access_key={}&query={}'.format(token,city)

    res = requests.get(url1)
    data = res.json()
    lat = data['data'][0]['latitude']
    print(lat)

    lon = data['data'][0]['longitude']
    print(lon)
    url2 = "http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}".format(lat, lon, TOKEN)
    res = requests.get(url2)
    data = res.json()

    data1 = int(data['list'][0]['main']['temp']) - 273
    data2 = int(data['list'][1]['main']['temp']) - 273
    data3 = int(data['list'][2]['main']['temp']) - 273
    data4 = int(data['list'][3]['main']['temp']) - 273
    data5 = int(data['list'][4]['main']['temp']) - 273

    x2 = [17, 18, 19, 20, 21]
    y2 = [data1, data2, data3, data4, data5]

    plt.plot(x2, y2, color='red', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='purple', markersize=12)

    plt.xticks(np.arange(min(x1), max(x1)+1, 1.0))


    plt.ylim(0, 21)
    plt.xlim(17, 21)

    plt.xlabel('Date')

    plt.ylabel('Temperature C')
    plt.title('Temp graph for the week')
    plt.savefig('graph.png')

    weatherdisplay.display()


weather.graph()


