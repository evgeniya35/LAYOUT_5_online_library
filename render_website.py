import os
import json

from math import ceil
from more_itertools import chunked
from jinja2 import Environment, FileSystemLoader, select_autoescape


def render_page(page, books, count_pages, current_page):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        books=books,
        count_pages=count_pages,
        current_page=current_page)
    with open(page, 'w', encoding='utf8') as file:
        file.write(rendered_page)


def make_pages():
    pages_folder = os.path.join(os.path.dirname(__file__), 'pages')
    os.makedirs(pages_folder, exist_ok=True)

    books_on_page = 10

    with open('books.json', 'r') as file:
        books_json = file.read()

    books = list(chunked(json.loads(books_json), 2))

    for number, books_page in enumerate(list(chunked(books, books_on_page)), 1):
        render_page(
            os.path.join(pages_folder, f'index{number}.html'),
            books_page,
            ceil(len(books) / books_on_page),
            number
            )


def main():
    make_pages()


if __name__ == '__main__':
    main()
