import requests
import re
import json
from tkinter import *
from tkinter import messagebox as mb


def check_balance(login, password):
    url="https://my3.webcom.mobi/json/balance.php"
    headers ={"Content-type": "text/json; charset=utf-8"}

    data = {"login": login,
            "password": password}
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            mb.showinfo("Баланс", f"Баланс счета {response_data["money"]}")
            return response_data["money"]
        else:
            mb.showerror("Ошибка!",f"Произошла ошибка проверки баланса {response.status_code}")
            return None
    except Exception as e:
        mb.showerror("Ошибка!",f"Произошла ошибка при проверке баланса {e}")


def validate_phone_number(phone_number):
    pattern = r'^79\d{9}$'
    return bool(re.match(pattern, phone_number))


def send_sms():
    user='python24'
    password='TCMS9L'
    sender='python2024'
    receiver = receiver_entry.get()
    text = text_entry.get(1.0, END)

    if len(text) > 160:
        mb.showerror("Ошибка!", f"Длина вашего сообщения {len(text)}. Она не может  превышать 160 символов.")
        return

    balance = check_balance(user, password)
    if balance:
        if float(balance) > 10:

            if not validate_phone_number(receiver):
                mb.showinfo("Ошибка!", "Некорректный номер телефона")
            else:
                url = f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}"
                try:
                    response = requests.get(url)

                    if response.status_code == 200:
                        mb.showinfo("Все хорошо!", "Сообщение успешно отправлено!")
                    else:
                        mb.showerror("Ошибка!", f"Ошибка при отправке {response.status_code}")
                except Exception as e:
                    mb.showerror("Ошибка!",f"Непредвиденная ошибка с кодом {e}")
        else:
            mb.showerror("Ошибка!","Недостаточно средств!")
    else:
        mb.showerror("Ошибка!","Не удалось получить информацию о балансе")

window = Tk()
window.title("Отправка СМС")
window.geometry("400x200")

Label(text="Номер получателя в формате 79*********: ").pack()
receiver_entry = Entry()
receiver_entry.pack()

Label(text="Введите текст СМС").pack()
text_entry = Text(height=6, width=30)
text_entry.pack()

send_button = Button(text="Отправить СМС", command=send_sms)
send_button.pack()

window.mainloop()




