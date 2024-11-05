import requests
import json

url="https://my3.webcom.mobi/json/balance.php"#адресный запрос с сайта
headers = {"Content-type": "text/json; charset=utf-8"}#заголовок с сайта

data = {"login": 'python24',
        "password": 'TCMS9L'}

try:
    response = requests.post(url, data=json.dumps(data), headers=headers)#отправляем запрос на сайт с параметрами

    if response.status_code == 200:#если выражение верно, то все хорошо
        response_data = response.json()
        print(response_data)
        print(f"Баланс: {response_data["money"]} руб.")#распечатываем баланс
    else:#если ошибка
        print(f"Произошла ошибка {response.status_code}")
except Exception as e:#обрабатываем исключения
    print(f"Произошла ошибка {e}")#распечатываем сообщение об ошибке