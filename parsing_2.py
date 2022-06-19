import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36'}


# Загрузка изображений
def download(url):
    resp = requests.get(url, stream=True)
    r = open('C:\\Users\\mavri\\Desktop\\Новая папка (2)\\' + url.split('/')[-1], 'wb')  # 'wb' это запись в байтах
    for value in resp.iter_content(1048576):  # Обём в килобайтах на один цикл (1 мб)
        r.write(value)
    r.close


# Фунция для получения ссылки на товар
def get_url():
    for count in range(1, 8):

        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"  # Меняем страницу по номеру

        response = requests.get(url, headers=headers)
        print(response)

        soup = BeautifulSoup(response.text, 'html.parser')

        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')  # Получаем данные карточки товара

        for i in data:  # создаём ссылку на каждую карточку товара
            card_url = 'https://scrapingclub.com' + i.find('a').get('href')
            print(card_url)
            yield card_url


# Получаем каждую страницу товара из функции и разбираем её
def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, 'lxml')  # Запрос на конкретную карточку

        data = soup.find('div', class_='card mt-4 my-4')  # Получаем данные карточки

        name = data.find('h3', class_='card-title').text

        descriprion = data.find('p', class_='card-text').text

        price = data.find('h4').text

        image = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')
        download(image)
        yield name, price, descriprion, image
