import requests#нам нужны будут запросы
import re#модуль для работы с регулярными выражениями
import json

def check_balance(login, password):#создаем функцию проверки баланса
    url="https://my3.webcom.mobi/json/balance.php"#адресный запрос с сайта
    headers = {"Content-type": "text/json; charset=utf-8"}#заголовок с сайта

    data = {"login": login,
            "password": password}#создаем переменную логина и пароля

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

def validate_phone_number(phone_number):#создаем функцию для проверки(validate) номера телефона
    pattern = r'^79\d{9}$'#проверяем номер телефона по шаблону
    return bool(re.match(pattern, phone_number))#возвращаем логическое значение:истину если номер верный и ложь если не верный.
    # и проверяет на соответствие, что шаблон есть в нашей строке


user='python24'#логин
password='TCMS9L'#пароль
sender='python2024'#подпись отправителя
receiver='79163439281'#номер телефона отправителя, начинающийся с семерки.
# используем для проверки правильности ввода
text='Hello world!'#сам текст сообщения, который отправляется

balance = check_balance(user, password)
if balance:#делаем проверку: если переменная balance не пустая
    if balance > 10:#если на балансе больше 10 рублей

        if not validate_phone_number(receiver):#вызываем функцию-validate_phone_number
        # и проверяем если номер телефона неверный
            print("Ошибка! Некорректный номер телефона")#распечатываем сообщение об этом
        else:#если же номер корректный
            url = f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}"
            # пишем ссылку по которой мы будем все это отправлять
            print(url)  # распечатываем в кансоль какое сообщение улетает в интернет
            try:  # пробуем отправить сообщение
                response = requests.get(url)  # получаем ответ(response) после того как отправили запрос(requests)
                print(response)  # распечатываем то что прилетит в ответ на наш запрос

                if response.status_code == 200:  # делаем проверку, если все хорошо
                    print("Сообщение успешно отправлено!")  # распечатываем сообщение об успешной отправке
                else:  # а если же что-то пошло не так
                    print(f"Ошибка при отправке{response.status_code}")  # распечатываем сообщение об ошибке
            except Exception as e:  # обрабатываем исключения
                print(f"Непредвиденная ошибка с кодом {e}")  # распечатываем сообщение об ошибке
    else:#если же баланс меньше 10 рублей
        print("Недостаточно средств!")#то сообщаем об этом пользователю
else:#если баланс пустой
    print("Не удалось получить информацию о балансе")#то сообщаем об этом




