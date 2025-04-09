# api-test-booking

### Настройка виртуальной среды:
- перейти в директорию проекта командой:
```shell
   cd api-test-booking
```
- создать виртуальную среду:
```shell
   python -m venv venv
```
- Активировать виртуальное окружение:

На Windows
```shell
   venv\Scripts\activate
```
На macOS и Linux
```shell
   source venv/bin/activate
```
- Установить pytest:
```shell
   pip install pytest
```
- Установить библиотеку requests:
```shell
   pip install requests
```
- Установить библиотеку faker для генерации случайных значений:
```shell
   pip install faker
```

## Запуск тестов:
#### Выполнить команду:
```shell
   pytest src/main.py
```
