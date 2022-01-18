import json

from more_itertools import chunked
from jinja2 import Environment, FileSystemLoader, select_autoescape


def render_books():
    with open('books.json', 'r') as file:
        books_json = file.read()
    books = list(chunked(json.loads(books_json)[:10], 2))

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    rendered_page = template.render(books=books)

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

def main():
    render_books()

if __name__ == '__main__':
    main()