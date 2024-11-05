import requests#нам нужны будут запросы
import re#модуль для работы с регулярными выражениями
import json
from tkinter import *
from tkinter import messagebox as mb


def check_balance(login, password):#создаем функцию проверки баланса
    url="https://my3.webcom.mobi/json/balance.php"#адресный запрос с сайта
    headers = {"Content-type": "text/json; charset=utf-8"}#заголовок с сайта

    data = {"login": login,
            "password": password}#создаем переменную логина и пароля

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)#отправляем запрос на сайт с параметрами

        if response.status_code == 200:#если выражение верно, то все хорошо
            response_data = response.json()
            mb.showinfo("Баланс", f"Баланс счета {response_data["money"]}")
            return response_data["money"]#возвращаем сообщение о балансе
        else:#если ошибка
            mb.showerror("Ошибка!",f"Произошла ошибка проверки баланса {response.status_code}")
            return None#при ошибке ничего не возвращается
    except Exception as e:#обрабатываем исключения
        mb.showerror("Ошибка!",f"Произошла ошибка при проверке баланса {e}")#распечатываем сообщение об ошибке

def validate_phone_number(phone_number):#создаем функцию для проверки(validate) номера телефона
    pattern = r'^79\d{9}$'#проверяем номер телефона по шаблону
    return bool(re.match(pattern, phone_number))#возвращаем логическое значение:истину если номер верный и ложь если не верный.
    # и проверяет на соответствие, что шаблон есть в нашей строке

def send_sms():
    user='python24'#логин
    password='TCMS9L'#пароль
    sender='python2024'#подпись отправителя
    receiver = receiver_entry.get()#получаем текст из поля ввода
    text = text_entry.get(1.0, END)#получаем текст из поля ввода от начала и до конца

    if len(text) > 160:#делаем проверку, если сообщение содержит больше 160 символов, то
        mb.showerror("Ошибка!", f"Длина вашего сообщения {len(text)}. Она не может превышать 160 символов")
        return #выходим из функции

    balance = check_balance(user, password)
    if balance:#делаем проверку: если переменная balance не пустая
        if float(balance) > 10:#если на балансе больше 10 рублей

            if not validate_phone_number(receiver):#вызываем функцию-validate_phone_number
            # и проверяем если номер телефона неверный
                mb.showinfo("Ошибка!", "Некорректный номер телефона")#распечатываем сообщение об этом
            else:#если же номер корректный
                url = f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}"
                # пишем ссылку по которой мы будем все это отправлять
                try:  # пробуем отправить сообщение
                    response = requests.get(url)  # получаем ответ(response) после того как отправили запрос(requests)

                    if response.status_code == 200:  # делаем проверку, если все хорошо
                        mb.showinfo("Все хорошо!", "Сообщение успешно отправлено!")  # распечатываем сообщение об успешной отправке
                    else:  # а если же что-то пошло не так
                        mb.showerror("Ошибка!", f"Ошибка при отправке{response.status_code}")  # распечатываем сообщение об ошибке
                except Exception as e:  # обрабатываем исключения
                    mb.showerror("Ошибка!",f"Непредвиденная ошибка с кодом {e}")  # распечатываем сообщение об ошибке
        else:#если же баланс меньше 10 рублей
            mb.showerror("Ошибка!","Недостаточно средств!")#то сообщаем об этом пользователю
    else:#если баланс пустой
        mb.showerror("Ошибка!","Не удалось получить информацию о балансе")#то сообщаем об этом

window = Tk()#создаем окно
window.title("Отправка СМС")#задаем заголовок окну
window.geometry("400x200")#задаем размер окну

Label(text="Номер получателя в формате 79*********: ").pack()#создаем метку
receiver_entry = Entry()#создаем поле ввода
receiver_entry.pack()

Label(text="Введите текст СМС").pack()
text_entry = Text(height=6, width=30)#создаем многострочное текстовое поле
text_entry.pack()

send_button = Button(text="Отправить СМС", command=send_sms)#создаем кнопку
send_button.pack()

window.mainloop()






