### Тестовое задание 
# REST API для расчета стоимости страхования

Сервис рассчитывает стоимость страхования в зависимости от типа груза, объявленной стоимости и даты.  
Стоимость рассчитывается по тарифам на даты и типы груза из файла `tariff.json`


### Используемые технологии:
* FastApi
* Tortoise ORM
* Postgresql
* Docker
* Docker-compose
* Python 3.11

В разработке использованы паттерны MVC и Service / Repository

### Скриншоты
![api_swagger](https://user-images.githubusercontent.com/109981473/254390640-4d1ea2dd-e68f-4881-8abb-87beb1a14aaf.png)
![api_swagger_post](https://user-images.githubusercontent.com/109981473/254391761-e8916b95-ab37-47df-83cb-a293cb5eeaeb.png)
![api_swagger_get](https://user-images.githubusercontent.com/109981473/254391971-6a35ffc6-3bb9-4037-9d94-05535563342b.png)

## Установка
* Клонируйте репозиторий 
```bash
git clone https://github.com/anshexa/insurance-fee-api.git
```
* Перейдите в директорию  
```bash
cd insurance-fee-api
```
### Перед запуском
* Создайте файл `.env` с переменными окружения по примеру файла `example.env`

* Установите зависимости из файла `requirements.txt`:
```bash
pip3 install -r requirements.txt
```

## Запуск через Docker
```bash
$ docker-compose build
```
```bash
$ docker-compose up
```
## Посмотреть документацию
можно в браузере по ссылке `http://127.0.0.1:8001/docs`

