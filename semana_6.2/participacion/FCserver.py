from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de vehículos
chocolates = {}


class Chocolate:
    def __init__(self, chocolate_type, price, flavor, stuffed=False):
        self.chocolate_type = chocolate_type
        self.price = price
        self.flavor = flavor
        self.stuffed = stuffed
        


class Tableta(Chocolate):
    def __init__(self, price, flavor):
        super().__init__("Tableta", price, flavor)

class Bombone(Chocolate):
    def __init__(self, price, flavor, stuffed=True):
        super().__init__("Bombone", price, flavor)

class Trufa(Chocolate):
    def __init__(self, price, flavor, stuffed=True):
        super().__init__("Trufa", price, flavor)


class Factory:
    @staticmethod
    def create_chocolate(chocolate_type, price, flavor):
        if chocolate_type == "tableta":
            return Tableta(chocolate_type, price, flavor)
        elif chocolate_type == "bombone":
            return Bombone(chocolate_type, price, flavor)
        elif chocolate_type == "trufa":
            return Trufa(chocolate_type, price, flavor)
        else:
            raise ValueError("Tipo de chocolate no válido")


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class Service:
    def __init__(self):
        self.factory = Factory()

    def add_vehicle(self, data):
        chocolate_type = data.get("chocolate_type", None)
        price = data.get("price", None)
        flavor = data.get("flavor", None)
        stuffed = data.get("stuffed", None)

        chocolate = self.factory.create_chocolate(
            chocolate_type, price, flavor
        )
        chocolates[len(chocolates) + 1] = chocolate
        return chocolate

    def list_vehicles(self):
        return {index: vehicle.__dict__ for index, vehicle in chocolates.items()}

    def update_vehicle(self, vehicle_id, data):
        if vehicle_id in vehicles:
            vehicle = vehicles[vehicle_id]
            plate_number = data.get("plate_number", None)
            capacity = data.get("capacity", None)
            if plate_number:
                vehicle.plate_number = plate_number
            if capacity:
                vehicle.capacity = capacity
            return vehicle
        else:
            raise None

    def delete_vehicle(self, vehicle_id):
        if vehicle_id in vehicles:
            del vehicles[vehicle_id]
            return {"message": "Vehículo eliminado"}
        else:
            return None


class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.delivery_service = Service()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/deliveries":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.add_vehicle(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/deliveries":
            response_data = self.delivery_service.list_vehicles()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/deliveries/"):
            vehicle_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.update_vehicle(vehicle_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Vehículo no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/deliveries/"):
            vehicle_id = int(self.path.split("/")[-1])
            response_data = self.delivery_service.delete_vehicle(vehicle_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Vehículo no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, yRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()
