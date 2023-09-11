import random
import requests

TOKEN = 'токен кума агая для проверки хахахв'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'

def send_message(chat_id, text):
    url = BASE_URL + 'sendMessage'
    params = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url, json=params)

def send_photo(chat_id, photo_url):
    url = BASE_URL + 'sendPhoto'
    params = {
        'chat_id': chat_id,
        'photo': photo_url
    }
    requests.post(url, json=params)

def handle_message(message):
    chat_id = message['chat']['id']
    user_number = int(message['text'])
    random_number = random.randint(1, 3)
    if user_number == random_number:
        send_message(chat_id, 'Правильно! Вы угадали!')
        send_photo(chat_id, 'https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
    else:
        send_message(chat_id, f'Неправильно! Я загадал число {random_number}. Попробуйте еще раз.')
        send_photo(chat_id, 'https://media.makeameme.org/created/sorry-you-lose.jpg')

def main():
    update_id = None
    while True:
        url = BASE_URL + 'getUpdates'
        if update_id:
            url += f'?offset={update_id + 1}'
        response = requests.get(url)
        data = response.json()
        for update in data['result']:
            if 'message' in update:
                handle_message(update['message'])
            update_id = update['update_id']

if name == 'main':
    main()