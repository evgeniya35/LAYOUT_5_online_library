from http import server
import re
from livereload import Server

from render_website import load_books

load_books()

server = Server()
server.watch('template.html', load_books)
server.serve(root='.')