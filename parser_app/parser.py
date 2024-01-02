import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://www.mashina.kg/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
}


@csrf_exempt
def get_html(url, params=''):
    request_car = requests.get(url, headers=HEADERS, params=params)
    return request_car


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='list-item list-label')
    cars = []
    for item in items:
        cars.append({
            'title': item.find('div', class_='block title').get_text(),
            'description': item.find('div', class_='block info-wrapper item-info-wrapper').get_text(),
            'price': item.find('div', class_='block price'),
        })
        return cars


@csrf_exempt
def parser_cars():
    html = get_html(URL)
    if html.status_code == 200:
        car_list = []
        for page in range(0, 1):
            html = get_html(f'https://www.mashina.kg/search/all/', params=page)
            car_list.extend(get_data(html.text))
        # return car_list
        print(car_list)
    else:
        raise Exception('Error in parse')


parser_cars()
