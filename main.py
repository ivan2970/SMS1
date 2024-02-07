import requests

user='python24'
password='TCMS9L'
sender='python2024'
receiver='79163439281'
text='Hello world!'

url=f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}"
print(url)
response = request.get(url)
print(response)

if response.status_code == 200:
    print("Сообщение успешно отправлено!")
else:
    print(f"Ошибка при отправке {response.status_code}")