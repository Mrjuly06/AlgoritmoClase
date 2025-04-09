def es_palindromo(numero):
    if 100 <= numero <= 999:  # Verifica que el número tenga tres cifras
        return str(numero) == str(numero)[::-1]
    else:
        return "El número debe ser de tres cifras."

# Solicitar número al usuario
numero = int(input("Ingrese un número de tres cifras: "))
resultado = es_palindromo(numero)

if resultado == True:
    print("El número es igual al revés (palíndromo).")
elif resultado == False:
    print("El número NO es igual al revés.")
else:
    print(resultado)
