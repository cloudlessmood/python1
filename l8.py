""" OpenWeatherMap (экспорт)
Сделать скрипт, экспортирующий данные из базы данных погоды,
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.
Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]

При выгрузке в html можно по коду погоды (weather.id) подтянуть
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions
Экспорт происходит в файл filename.
Опционально можно задать в командной строке город. В этом случае
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.
"""

import json
import urllib.request

try:
    def url_builder():
        city_id = input("Write the city ID: ")
        user_api = ''
        unit = 'metric'
        api = 'http://api.openweathermap.org/data/2x.5/weather?id='
        full_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
        return full_url


    def get_data(full_url):
        url = urllib.request.urlopen(full_url)
        output = url.read()
        data = json.loads(output)
        url.close()
        return data


    with open("filename.txt", "w") as file:
        'Weather in: {}, {}:'.format(data.get('name'), data.get('sys').get('country'))
        data.get('main').get('temp')
        data['weather'][0]['main']
        'Max: {}, Min: {}'.format(data.get('main').get('temp_max'), data.get('main').get('temp_min'))
        'Wind Speed: {}'.format(data.get('wind').get('speed'))
        'Humidity: {}'.format(data.get('main').get('humidity'))
        'Cloud: {}'.format(data.get('clouds').get('all'))
        'Pressure: {}'.format(data.get('main').get('pressure'))
        'Sunrise at: {}'.format(data.get('sys').get('sunrise'))
        'Sunset at: {}'.format(data.get('sys').get('sunset'))

except:
    "We do not have such city ID"