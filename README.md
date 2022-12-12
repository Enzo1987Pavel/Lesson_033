# Python_diploma

### Lesson 38
##
* ![version](https://img.shields.io/badge/Python-v_3.10-informational/?style=social&logo=Python)
* ![version](https://img.shields.io/badge/Django-v_4.0.1-informational/?style=social&logo=Django)
* ![version](https://img.shields.io/badge/PostgreSQL-v_14.6_alpine-informational/?style=social&logo=Postgresql)
* ![version](https://img.shields.io/badge/Docker_Desktop-v_4.14.1-informational/?style=social&logo=Docker)
##
#### Файл `"docker-compose.yaml"` содержит контейнер с базой данных Postgres, который разворачивается при вызове в терминале команды `docker-compose up -d`.
#### Файл `"docker-compose-ci.yaml"` для разворачивания приложения на сервере.

#### Также содержится файлы *`".env"`* и *`".env_ci"`* для хранения переменных среды. Файл *`".env_ci"`* содержит в себе переменные окружения, но замененные на плейсхолдеры.
##
#### Активация виртуального окружения:
```sh
.\venv\Scripts\Activate
```

#### Описана абстрактная модель пользователя, в Админке изменены названия и заголовки в самой Админке.
#### Создан файл _requirements.txt_ для установки зависимостей в приложении через команду:
```sh
pip freeze > requirements.txt
```
#### Установка зависимостей из _requirements.txt_:
```sh
pip install -r requirements.txt
```
