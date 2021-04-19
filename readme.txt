Данный web проект ялвяеться парсером для сайта https://hh.ru/employer

Установка

В первую очередь клонируем репозиторий https://github.com/Albert9595/test

Далее заходим в проект и запускаем виртуальное окружение:  source parser/bin/activate

Устанавливаем библиотеки с requirements.txt : pip install -r requirements.txt

Затем  переходим в Django проект parser_info_from_web:  cd parser_info_from_web

Запускаем проект: python manage.py runserver

Открыть вторую консоль и запускаем redis : docker-compose up (изначально у вас должен быть настроен docker)

Открываем третью консоль и также переходим в Django проект parser_info_from_web: cd parser_info_from_web

Запускаем celery : celery -A parser_info_from_web worker -l INFO

Открываем браузер и вписываем в url, http://127.0.0.1:8000/ (если вы запустили Django проект на другом порту поставьте свой порт)

Парсер парсит данные с https://api.hh.ru/vacancies (работает только с Российской Федерацией)

Посмотреть все Республики можно в areas.txt

Открывается пустая страница, чтобы запустить парсер, в поле City: введите город в поле Vacans: вакансию, затем нажмите найти

Подождите несколько секунд и обновите страницу

Что бы удалить данные перейдите по ссылке http://127.0.0.1:8001/admin/

loggin: admin
password: admin

Выберите пункт Job vacancies и Выберите вакансии которые хотите удалить

