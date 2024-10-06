# Sumamos en Python!
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # Realizar la suma
    resultado = num1 + num2

    print(f"La suma de {num1} y {num2} es: {resultado}")

except ValueError:
    print("Por favor, ingresa un número válido.")

