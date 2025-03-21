# Diploma-work

## Проект автотестов для сервиса Кинопоиск

### Стек:
- pytest
- selenium
- requests
- allure
- config

### Струткура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)

### Шаги
1. Склонировать проект 'git clone https://github.com/AnnaNovak/Diploma-work
   pytest_ui_api_template.git'
2. Установить зависимости
3. Запустить тесты 'pytest'

### Библиотеки (!)
- pyp install pytest
- pip install selenium
- pip install webdriver-manager

### Команды для запуска тестов
- Для запуска тестов команда: python -m pytest api_tests ui_tests

Для отображения отчета allure: allure serve allure-results

### Включенные тесты
## UI
# login
При выполнении теста необходимо ввести код, который придет на ваш номер телефона