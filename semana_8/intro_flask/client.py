import requests

url = 'http://localhost:5000/'

response = requests.get(url)

def reply(response):
    if response.status_code == 200:
        data = response.json()
        mensaje = data['mensaje']
        print("Respuesta del servidor (GET):", mensaje)
    else:
        print("Error al conectar con el servidor (GET):", response.status_code)
if response.status_code == 200:
    print(response.text)
else:
    print("Error al conectar con el servidor:", response.status_code)

params = {'nombre': 'Maycol'}
response = requests.get(url+'saludar', params=params)
reply(response)

params = {'num1': "5", 'num2': "3"}
response = requests.get(url+'sumar', params=params)
reply(response)

params ={ 'cadena': 'reconocer'}
response = requests.get(url+'palindromo', params=params)
reply(response)

params = {'cadena': 'excepciones', 'vocal': 'e'}
response = requests.get(url+'contar', params=params)
reply(response)
# if response.status_code == 200:
#     data = response.json()
#     mensaje = data['mensaje']
#     print("Respuesta del servidor (GET):", mensaje)
# else:
#     print("Error al conectar con el servidor (GET):", response.status_code)
