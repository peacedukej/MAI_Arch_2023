# Вариант 5: Мессенджер

## Приложение должно содержать следующие данные:
- Пользователь
- Групповой чат
- PtP Чат

## Реализовать API:
- Создание нового пользователя
- Поиск пользователя по логину
- Поиск пользователя по маске имя и фамилии
- Создание группового чата
- Добавление пользователя в чат
- Добавление сообщения в групповой чат
- Загрузка сообщений группового чата
- Отправка PtP сообщения пользователю
- Получение PtP списка сообщения для пользователя

# Задание 1

## Цель
- Ознакомиться с инструментами проектирования в формате Architecture As A Code.
- Получить практический навык в моделировании в нотации C4.

## Задание
1. **Установка инструментов**
   - Клиент Git
   - Текстовый редактор (рекомендуется Visual Studio Code)
   - Плагины к Visual Studio Code C4 DSL

2. **Регистрация на GitHub**
   - Зарегистрироваться на [github.com](https://github.com) (если еще нет учетной записи)

3. **Создание репозитория**
   - Создать публичный репозиторий для выполнения практической работы у себя в аккаунте

4. **Клонирование репозитория**
   - Скопировать репозиторий [hl_mai_lab_00](https://github.com/DVDemon/hl_mai_lab_00) с примерами задания

5. **Создание описания архитектуры**
   - Создать файлы с описанием "архитектуры" согласно вашему варианту задания в [Structurizr Lite](https://structurizr.com/lite)

6. **Требования к диаграммам**
   - Должна быть контекстная диаграмма
   - Должна быть диаграмма контейнеров
   - Должна быть диаграмма развертывания
   - Должно быть несколько динамических диаграмм


# Задание 2

## Цель
- Получение практических навыков в построении сервисов, работающих с реляционными данными.

## Задание
Разработать приложение, осуществляющее хранение данных о пользователях в реляционной СУБД. Для выявленных в предыдущем задании вызовов между сервисами создайте REST интерфейс.

## Условия выполнения
- Данные должны храниться в СУБД PostgreSQL.
- Должны быть созданы таблицы для каждой сущности из вашего задания.
- Интерфейс к сущностям должен предоставляться в соответствии со стилем REST.
- API должен быть специфицирован в OpenAPI 3.0 (должен храниться в index.yaml).
- Должен быть создан скрипт по созданию базы данных и таблиц, а также наполнению СУБД тестовыми значениями.
- Для сущности, отвечающей за хранение данных о пользователе (клиенте), для пользователей должен быть реализован интерфейс поиска по маске фамилии и имени, а также стандартные CRUD операции.
- Данные о пользователе должны включать логин и пароль. Пароль должен храниться в закрытом виде (хэширован).

## Рекомендуемая последовательность выполнения работы:
1. Создайте схему БД.
2. Создайте таблицы.
3. Создайте скрипт для первичного наполнения БД и выполните.
4. Реализуйте REST-сервис.
5. Сделайте спецификацию с OpenAPI с помощью Postman и сохраните ее в index.yml.
6. Протестируйте сервис.
7. Создайте Dockerfile для вашего сервиса.
8. Протестируйте его работу в Docker.
9. Опубликуйте проект на GitHub.