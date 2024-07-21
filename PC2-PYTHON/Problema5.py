def num_primo(n):
    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sumar_primos = sum(n for n in range(2, 100) if num_primo(n))
print("La suma de todos los números primos menores que 100 es: ", sumar_primos)