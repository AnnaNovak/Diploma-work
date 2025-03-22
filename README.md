# Diploma-work

## Проект автотестов для сервиса Кинопоиск

### Стек:
- pytest
- selenium
- requests
- allure
- config

### Струткура:
-   Diploma-work
  - api
    - clients
        - kinopoisk_client.py
    - tests
      - test_kinopoisk_empty_search.py
      - test_kinopoisk_invalid_method.py
      - test_kinopoisk_search_by_genre.py
      - test_kinopoisk_search_by_id.py
      - test_kinopoisk_search_by_title.py
      - test_kinopoisk_search_by_year.py
  - config
      - settings.py
  - ui
    - pages
       - base_page.py
       - kinopoisk_login_page.py
       - kinopoisk_search_page.py
       - main_page.py
    - tests
       - conftest.py
       - test_kinopoisk.py
       - test_kinopoisk_login.py
   - .gitignore
   - README.md
   - requirements.txt

### Шаги
1. Склонировать проект https://github.com/AnnaNovak/Diploma-work.git
2. Установить зависимости
3. Запустить тесты 'pytest'

### Библиотеки (!)
- pyp install pytest
- pip install selenium
- pip install webdriver-manager

### Включенные тесты
## UI 
При выполнении тестов необходимо вручную наживать на капчу "я не робот"
# login
При выполнении теста необходимо ввести код, который придет на ваш номер телефона