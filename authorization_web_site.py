from requests import Session
from bs4 import BeautifulSoup

headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36'}

work = Session()

work1 = work.get('http://quotes.toscrape.com', headers=headers)

response = work.get('http://quotes.toscrape.com/login', headers=headers)

soap = BeautifulSoup(response.text, 'html.parser')

token = soap.find('form').find('input').get('value')  # Получаем токен для авторизации

print('Токен - ' + token)

data = {'csrf_token': token,
        'username': 'mavric',
        'password': '123'}

result = work.post('http://quotes.toscrape.com/login', headers=headers, data=data, allow_redirects=True)

text = soap.find_all('span', class_='text')
print(text)
# for i in quote:
#     if len(quote) != 0:
#         spisok.append(quote)

#     else:
#         break
