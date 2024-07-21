Inicio = 1500
Fin = 2700

Numero = Inicio
Num_divisibles = []

while Numero <= Fin:
    
    if Numero % 7 == 0 and Numero % 5 == 0:
        Num_divisibles.append(Numero)
    
    Numero+= 1

print("Los números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son: ")
print(Num_divisibles)