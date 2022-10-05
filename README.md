# Тренировочный проект автотестов на [Rick and Morty API](https://rickandmortyapi.com/)

## <img src="https://github.com/ioomoon/QA-guru-graduation/blob/master/img/icon5.png?raw=true" width="20"> Реализованы проверки:
- Проверка статус кода и валидация ответа при запросе всех персонажей
- Проверка статус кода и валидация ответа при запросе конкретного персонажа по полю id 
- Проверка статус кода и валидация ответа при запросе нескольких персонажей по полю id (с параметрами)
- Проверка статус кода и валидация ответа при запросе персонажа с несуществующим id (с параметрами)
- Проверка статус кода и валидация ответа при запросе персонажа с некорректным id (с параметрами)
- Проверка статус кода и валидация ответа при запросе персонажа с фильтром по полю name (с параметрами)
- Проверка статус кода и валидация ответа при запросе персонажей с несуществующим значением фильтра поля name
- Проверка статус кода и валидация ответа при запросе персонажей с фильтром по нескольким полям (с параметрами)
- Проверка статус кода и валидация ответа при запросе персонажей с несуществующими значениями фильтров по нескольким полям (с параметрами)

## <img src="https://github.com/ioomoon/QA-guru-graduation/blob/master/img/icon4.png?raw=true" width="20"> Запуск проекта:
- Запуск проекта локально:
```bash
pytest -v -k tests --alluredir=[path_to_report_dir]
```
- Для генерации Allure-репорта:
```bash
allure serve [path_to_report_dir]
```

## <img src="https://github.com/ioomoon/QA-guru-graduation/blob/master/img/icon6.png?raw=true" width="20"> Отчеты в Allure Report
![](img/Allure_report_5.png "status and severity")
![](img/Allure_report_2.png "suites")
![](img/Allure_report_3.png "retries")
![](img/Allure_report_4.png "retries with fail")



<img align="center" src="https://github.com/ioomoon/RickAndMortyApiTests/blob/master/img/Rick_and_Morty_logo.png">

