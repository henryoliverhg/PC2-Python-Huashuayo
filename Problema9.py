def OmitirVocales(texto):
    Vocales = "aeiouAEIOU"
    Resultado = ''.join([letra for letra in texto if letra not in Vocales])
    return Resultado

Ingreso = input("Ingrese una cadena de texto: ")
Salida = OmitirVocales(Ingreso)

print("El texto sin vocales es: ", Salida)