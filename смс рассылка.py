import requests#нам нужны будут запросы
from bottle import response

user='python24'#логин
password='TCMS9L'#пароль
sender='python2024'#подпись отправителя
receiver='79163439281'#номер телефона отправителя, начинающийся с семерки.
# используем для проверки правильности ввода
text='Hello world!'#сам текст сообщения, который отправляется

url=f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}"
#пишем ссылку по которой мы будем все это отправлять
print(url)#распечатываем в кансоль какое сообщение улетает в интернет
response = request.get(url)#получаем ответ(response) после того как отправили запрос(requests)
print(response)#распечатываем то что прилетит в ответ на наш запрос

if response.status_code == 200:#делаем проверку, если все хорошо
    print("Сообщение успешно отправлено!")#распечатываем сообщение об успешной отправке
else:#а если же что-то пошло не так
    print(f"Ошибка при отправке{response.status_code}")#распечатываем сообщение об ошибке
