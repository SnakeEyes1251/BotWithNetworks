import requests
import logging
import time

from config import TOKEN

def post_q(query: str, user_id: str, network_id):
    url = "https://api.coze.com/v3/chat"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    prompt = {
        "bot_id": f"{network_id}",
        "user_id": f"{user_id}",
        "stream": False,
        "auto_save_history": True,
        "additional_messages": [
            {"role": "user",
             "content": f"{query}",
             "content_type": "text"}
        ]
    }

    try:
        response = requests.post(url=url, headers=headers, json=prompt)
        response.raise_for_status()  # Проверка на HTTP ошибки
        response_data = response.json()
        chat_id = response_data['data']['id']
        conversation_id = response_data['data']['conversation_id']
        return chat_id, conversation_id
    except Exception as e:
        logging.error(f"Exception in post_q: {e}")
        return None, None
    
def post_with_ids(query: str, user_id: str, chat_id, conversation_id):
    url = f"https://api.coze.com/v3/chat?chat_id={chat_id}&conversation_id={conversation_id}"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    prompt = {
        "bot_id": "7398164582218842117",
        "user_id": f"{user_id}",
        "stream": False,
        "auto_save_history": True,
        "additional_messages": [
            {"role": "user",
             "content": f"{query}",
             "content_type": "text"}
        ]
    }

    try:
        response = requests.post(url=url, headers=headers, json=prompt)
        response.raise_for_status()  # Проверка на HTTP ошибки
        response_data = response.json()
        chat_id = response_data['data']['id']
        conversation_id = response_data['data']['conversation_id']
        return chat_id, conversation_id
    except Exception as e:
        logging.error(f"Exception in post_witn_ids: {e}")
        return None, None

def status(chat_id: str, conversation_id: str):
    url = f"https://api.coze.com/v3/chat/retrieve?chat_id={chat_id}&conversation_id={conversation_id}"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()  # Проверка на HTTP ошибки
        response = response.json()
        print(response)
        return response['data']['status']
    except Exception as e:
        logging.error(f"Exception in status: {e}")
        return None

def get_status(chat_id: str, conversation_id: str) -> bool:
    if chat_id and conversation_id:
        while True:
            status_result = status(chat_id, conversation_id)
            if status_result is None:
                return False 

            if status_result == "completed":
                return True
            
            if status_result == "failed":
                return False
            
            print(status_result)
            time.sleep(1)  # Ждем 5 секунд перед следующим запросом
    return False

def get_answ(chat_id: str, conversation_id: str):
    url = f"https://api.coze.com/v3/chat/message/list?chat_id={chat_id}&conversation_id={conversation_id}"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    if get_status(chat_id, conversation_id):
        try:
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()  # Проверка на HTTP ошибки
            response_data = response.json()
            
            # Проверяем структуру ответа
            if 'data' in response_data and isinstance(response_data['data'], list):
                # Извлекаем содержимое из первого элемента списка
                for message in response_data['data']:
                    if message.get('type') == 'answer':
                        return message.get('content')  # Возвращаем содержимое ответа
            else:
                logging.error("Unexpected response structure: %s", response_data)
                return None  # Возвращаем None, если структура не соответствует ожиданиям
        except Exception as e:
            logging.error(f"Exception in get_answ: {e}")
            return None  # Возвращаем None в случае ошибки    
    return None