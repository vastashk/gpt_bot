import os
import openai
from dotenv import load_dotenv

# Загрузка переменных из .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Проверка наличия ключа API
if not api_key:
    print("Ошибка: API ключ не найден. Проверьте .env файл.")
    exit(1)

openai.api_key = api_key

def send_query_to_chatgpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  
            messages=[{"role": "user", "content": prompt}],

        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Ошибка при запросе к ChatGPT: {e}"

def main():
    print("Консольный интерфейс ChatGPT")
    print("Введите 'exit', чтобы выйти.")
    
    while True:
        user_input = input("Ваш запрос: ")
        if user_input.lower() == 'exit':
            print("Выход из программы.")
            break
        response = send_query_to_chatgpt(user_input)
        print(f"Ответ ChatGPT:\n{response}\n")

if __name__ == "__main__":
    main()
