import os
import json

from more_itertools import chunked
from jinja2 import Environment, FileSystemLoader, select_autoescape


def render_page(page, books):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(books=books)
    with open(page, 'w', encoding='utf8') as file:
        file.write(rendered_page)


def load_books():
    pages_folder = os.path.join(os.path.dirname(__file__), 'pages')
    os.makedirs(pages_folder, exist_ok=True)

    with open('books.json', 'r') as file:
        books_json = file.read()
    books = list(chunked(json.loads(books_json), 2))
    
    for i, books_page in enumerate(list(chunked(books, 10)), 1):
        render_page(
            os.path.join(pages_folder, f'index{i}.html')
            ,books_page
            )


def main():
    load_books()

if __name__ == '__main__':
    main()