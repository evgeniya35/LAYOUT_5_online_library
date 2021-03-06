# Сайт публикации книг

Программа формирования страниц сайта скачанных книг online библиотеки [БОЛЬШАЯ БЕСПЛАТНАЯ БИБЛИОТЕКА tululu.org](https://tululu.org/). 

[Демонстрационная версия сайта скачанных книг](https://evgeniya35.github.io/LAYOUT_5_online_library/pages/index1.html)

Программа скачивания книг размещена в [репозитории](https://github.com/evgeniya35/LAYOUT_4_online_library-.git). Для скачивания книг следуйте инструкции репозитория.

## Как установить

### Окружение
Python должен быть установлен.

### Установка
Установите программу из репозитория:
```bash
git clone https://github.com/evgeniya35/LAYOUT_5_online_library.git

```

### Зависимости
Используйте pip для установки зависимостей:
```bash
pip install -r requirements.txt
```


 ## Запуск

Для формирования страниц сайта требуются каталог `media` содержащий скачанные книги, обложки и файл описания `books.json`. Программа скачивания и описание размещены в [репозитории](https://github.com/evgeniya35/LAYOUT_4_online_library-.git). 
Разместите предварительно скачанные каталог `media` и файл `books.json` в каталоге проекта публикации книг.

- Для запуска скрипта формирования страниц, используйте командную строку:
```bash
$ python server.py
```
Перейдите по ссылке локального WEB сервера [http://127.0.0.1:5500/pages/index1.html](http://127.0.0.1:5500/pages/index1.html)

![GIF сайта](local-site.gif)


- Возможно формирование страниц без запуска локального WEB сервера. Используйте:
```bash
$ python render_website.py
```
Используйте сформированные в каталоге `pages` html страницы для размещения в своих проектах.


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
