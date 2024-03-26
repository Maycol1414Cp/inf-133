import requests

url = 'http://localhost:8000/pizzas'
headers = {'Content-Type': 'application/json'}

#GET /pizzas
response = requests.get(url)
print(response.json())

#POST /pizzas
mi_pizza={
    'tamaño':'mediana',
    'masa':'tradicional',
    'toppings':['pepperoni','piña']
}
response = requests.post(url, json=mi_pizza, headers=headers)
print(response.json())

# PUT /pizzas/1
edit_pizza = {
    "tamaño": "Mediano",
    "masa": "Gruesa",
    "toppings": ["Pepperoni", "Queso"]
}
response = requests.post(url, json=edit_pizza, headers=headers)
print(response.json())


# PUT /pizzas/1
edit_pizza = {
    "tamaño": "Mediano",
    "masa": "Gruesa",
    "toppings": ["Pepperoni", "Queso"]
}

# DELETE /pizzas/1

response = requests.delete(url + "/1")
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())