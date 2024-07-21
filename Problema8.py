def Factorial(n):
    
    if n < 0:
        return "El número ingresado debe ser un entero no negativo"
    if n == 0 or n == 1:
        return 1
    Resultado = 1
    for i in range(2, n + 1):
        Resultado *= i
    return Resultado

Num = int(input("Ingrese un número entero no negativo: "))
print("El factorial de", Num, "es", Factorial(Num))