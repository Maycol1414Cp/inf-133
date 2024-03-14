from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
estudiantes = [
    {
        "id": 1,
        "nombre": "jhon",
        "apellido": "Gallardo",
        "carrera": "Desarrollo de Software",
    },
    {
        "id": 2,
        "nombre": "Gabriela",
        "apellido": "Torrez",
        "carrera": "Economia",
    },
    {
        "id": 3,
        "nombre": "Jorge",
        "apellido": "Rojas",
        "carrera": "Economia",
    },
    {
        "id": 4,
        "nombre": "Maria",
        "apellido": "Blanco",
        "carrera": "Informatica",
    },
]


class RESTRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, error_code, data):
        self.send_response(error_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
    def do_GET(self):
        parse_path=urlparse(self.path)
        query_params=parse_qs(parse_path.query)
        print(query_params)

        if parse_path.path=="/estudiantes":
            if "nombre" in query_params:
                nombre=query_params["nombre"][0]
                estudiantes_filtrados=[
                    estudiante 
                    for estudiante in estudiantes 
                    if estudiante["nombre"]==nombre
                ]
                if estudiantes_filtrados:
                    self.response_handler(200,estudiantes_filtrados)
                else:
                    self.response_handler(204,[])
            else:
                self.response_handler(200,estudiantes)
        if self.path == "/estudiantes":
            self.response_handler(200, estudiantes)
            # self.send_response(200)
            # self.send_header("Content-type", "application/json")
            # self.end_headers()
            # self.wfile.write(json.dumps(estudiantes).encode("utf-8"))

        elif self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                self.reqwuest_handler(200, estudiante)
                # self.send_response(200)
                # self.send_header("Content-type", "application/json")
                # self.end_headers()
                # self.wfile.write(json.dumps(estudiante).encode("utf-8"))
        elif(self.path == "/carreras"):
            carreras_totales = []
            for estudiante in estudiantes:
                if estudiante["carrera"] not in carreras_totales:
                    carreras_totales.append(estudiante["carrera"])
            if (carreras_totales):
                self.request_handler(200, carreras_totales)
                # self.send_response(200)
                # self.send_header("Content-type", "application/json")
                # self.end_headers()
                # self.wfile.write(json.dumps(carreras_totales).encode("utf-8"))
    
        elif(self.path.startswith("/carreras/")):
            carrera = (self.path.split("/")[-1]).lower()
            estudiante_carrera = filter( lambda estudiante: estudiante["carrera"].lower() == carrera,estudiantes)
            if (estudiante_carrera):
                self.request_handler(200, estudiante_carrera)
                # self.send_response(200)
                # self.send_header("Content-type", "application/json")
                # self.end_headers()
                # self.wfile.write(json.dumps(list(estudiante_carrera)).encode("utf-8"))       
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_POST(self):
        if self.path == "/estudiantes":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.response_handler(201, estudiantes)
            # self.send_response(201)
            # self.send_header("Content-type", "application/json")
            # self.end_headers()
            # self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})
            # self.send_response(404)
            # self.send_header("Content-type", "application/json")
            # self.end_headers()
            # self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_PUT(self):
        if self.path.startswith("/estudiantes"):
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            id = data["id"]
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                estudiante.update(data)
                self.response_handler(200, estudiante)
                # self.send_response(200)
                # self.send_header("Content-type", "application/json")
                # self.end_headers()
                # self.wfile.write(json.dumps(estudiante).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_DELETE(self):
        if self.path == "/estudiantes":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            estudiantes.clear()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()