from flask import Flask, request, jsonify
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route('/saludar', methods=['GET'])
def saludar():
    nombre = request.args.get('nombre')
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400
            )
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})


@app.route('/sumar', methods=['GET'])
def sumar():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    if not num1 and num2:
        return (
            jsonify({"error": "Se requiere un num1 y un num2 en los parámetros de la URL."}),
            400
            )

    elif not num1:
        return (
            jsonify({"error": "Se requiere un num1 en los parámetros de la URL."}),
            400
            )
    elif not num2:
        return (
            jsonify({"error": "Se requiere un num2 en los parámetros de la URL."}),
            400
            )
    else:
        return jsonify({"mensaje": f"el resultado de {num1} + {num2} es:{num1+num2}"})


@app.route('/palindromo', methods=['GET'])
def palindromo():
    cad = request.args.get('cadena')
    if not cad:
        return (
            jsonify({"error": "Se requiere una cadena en los parámetros de la URL."}),
            400
            )
    if cad == cad[::-1]:
        return jsonify({"mensaje": f"la palabra: {cad} es palindromo"})
    else: 
        return jsonify({"mensaje": f"la palabra: {cad} no es palindromo"})
    
@app.route('/contar', methods=['GET'])
def contar():
    cad = request.args.get('cadena')
    voc = request.args.get('vocal')
    if not cad:
        return (
            jsonify({"error": "Se requiere una cadena en los parámetros de la URL."}),
            400
            )
    elif not voc:
        return (
            jsonify({"error": "Se requiere una vocal en los parámetros de la URL."}),
            400
            )
    elif not voc and cad:
        return (
            jsonify({"error": "Se requiere una vocal y una cadena en los parámetros de la URL."}),
            400
            )
    cont=0
    for c in cad:
        if c==voc:
            cont+=1
    return jsonify({"mensaje": f"la cantidad de la vocal {voc} en la cadena {cad} es: {cont}"})

if __name__ == '__main__':
    app.run(debug=True)
