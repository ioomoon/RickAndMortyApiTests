# Тренировочный проект автотестов на [Rick and Morty API](https://rickandmortyapi.com/)

## <img src="https://github.com/ioomoon/QA-guru-graduation/blob/master/img/icon2.png?raw=true" width="25"> Стек технологий:


## <img src="https://github.com/ioomoon/QA-guru-graduation/blob/master/img/icon5.png?raw=true" width="20"> Реализованы проверки:
- Проверка статус кода и валидация ответа при запросе 
    - всех персонажей
    - конкретного персонажа по полю id 
    - нескольких персонажей по полю id (параметризован)
    - персонажа с несуществующим id (параметризован)
    - персонажа с некорректным id (параметризован)
    - персонажа с фильтром по полю name (параметризован)
    - персонажей с несуществующим значением фильтра поля name
    - персонажей с фильтром по нескольким полям (параметризован)
    - персонажей с несуществующими значениями фильтров по нескольким полям (параметризован)

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
- Графики
![](img/Allure_report_5.png "status and severity")
- Тестовые наборы
![](img/Allure_report_2.png "suites")
- История запуска теста
![](img/Allure_report_3.png "retries")
![](img/Allure_report_4.png "retries with fail")
  
<img align="center" src="https://github.com/ioomoon/RickAndMortyApiTests/blob/master/img/Rick_and_Morty_logo.png">
