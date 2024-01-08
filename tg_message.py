TOKEN = "6390462747:AAFEcJVIwVkmpO-BuiiBrAb-2-SJ4c-3kc4"
import requests

def send_message(first_name, last_name, email, message):
    URL = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage'
    chat_id = "511893166"
    text = f'{first_name} {last_name}\n{email}\n{message}'
    data = {'chat_id': chat_id, 'text': text}
    return requests.post(URL, data=data)
