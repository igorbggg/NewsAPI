# NewsAPI - Интерфейс к базе для Frontend

## Запуск
1. Перед запуском необходимо установить зависимости:  
`pip install -r requirements.txt`

2. В корне проекта необходимо создать файл `.env.prod`, 
скопировав `.env.sample` и заполнить необходимые параметры.

3. Запустить приложение:
`python -s main.py`


## Docker

1. Повторить шаг 2 из раздела "Запуск"
2. Выполнить команды:  
`docker build -t news-api .`  
`docker run -d -p 8080:8080 news-api`  

