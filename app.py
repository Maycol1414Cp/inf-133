from http.server import HTTPServer, SimpleHTTPRequestHandler
def run(server_addres=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    try:
        server_addres=('',8000)
        httpd=server_class(server_addres,handler_class)
        print("inciando servidor web en http://localhost:8000/")
        httpd.server_forever()
    except KeyboardInterrupt:
        print('apagando el servidor')
        httpd.socket.close()
if _name_ == "_main_":
    run()    