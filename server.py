from http import server
import re
from livereload import Server

from render_website import render_books

render_books()

server = Server()
server.watch('template.html', render_books)
server.serve(root='.')