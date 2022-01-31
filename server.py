from livereload import Server
from render_website import make_pages

make_pages()

server = Server()
server.watch('template.html', make_pages)
server.serve(root='.', default_filename='pages/index1.html')
