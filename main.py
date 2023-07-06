# Solicitar al usuario que ingrese un número entero no negativo
numero = int(input("Por favor, ingresa un número entero no negativo: "))

# Definir la función factorial
def factorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

# Calcular el factorial utilizando la función factorial
factorial_numero = factorial(numero)

# Imprimir el resultado del cálculo del factorial
print("El factorial de", numero, "es:", factorial_numero)

if __name__ == '__main__':
    app.host()

@app.post('/inference', status_code=200)
def inference(doc: Document):
    respuesta, tokens = inference(doc.prompt)
    return {
        'interface': response[0],
        'usage': response[1]
    }