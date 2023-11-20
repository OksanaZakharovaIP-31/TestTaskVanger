# TestTaskVanger
Тестовое задание от компании Вангер.рф

# Запуск приложения

1. Клонирование репозитория

`https://github.com/OksanaZakharovaIP-31/TestTaskVanger.git`

2. Установка виртуального окружения и его активация

`python -m venv venv`

`venv\Scripts\activate.bat` - Windows

`source venv/bin/activate` - Linux and MacOS

3. Установка зависимостей

`pip install -r req.txt`

4. База данных - MySQL
5. Все ключи, пароли храняться в файле .env (создать в папке проекта) (заполнить для себя)

```
NAME='your name db'
USER=root
PASSWORD='your password'
HOST=localhost
PORT=3306
```

6. Запуск миграций
```
python namage.py makemigrations
python manage.py migrate
```

7. Запуск проекта

`python manage.py runserver`

8. Отображение страницы

Перейти по [ссылке](http://127.0.0.1:8000/)
