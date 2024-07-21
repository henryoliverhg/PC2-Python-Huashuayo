a, b = 0, 1
Fibonacci = []

while a <= 50:
    Fibonacci.append(a)
    a, b = b, a + b

print("La serie de Fibonacci entre 0 y 50 es: ", Fibonacci)