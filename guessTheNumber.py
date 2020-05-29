"""
Hacer en Python un programa que:
1. Al ejecutarse genera un numero de 1 a 50.
2. Saca un prompt para que el usuario intente adivinar el numero generado.
3. Por cada intento decimos al usuario si está por encima o por debajo y le damos la opción de intentar otra vez.
4. Si acierta, le decimos que muy bien y termina el juego. Si falla 5 veces le indicamos que ha fracasado.
Si se puede, hacer tests unitarios.
"""

from random import randint

randomNumberToGuess = randint(1,50)
userNumber = None
tries = 0
maxNumberOfTries = 5

print ("He generado un número entre 1 y 50. Tienes " + str(maxNumberOfTries) + " oportunidades para acertarlo. Adivínalo!")

while (userNumber != randomNumberToGuess):
    userNumber = int(input("Introduce un número entre 1 y 50: "))

    if userNumber == randomNumberToGuess:
        print ("Muy bien, has acertado el número")
    if userNumber > randomNumberToGuess:
        print ("El número que buscamos es menor que " + str(userNumber))
    if userNumber < randomNumberToGuess:
        print ("El número que buscamos es mayor que " + str(userNumber))
    tries = tries + 1
    if tries == maxNumberOfTries and userNumber != randomNumberToGuess:
        print("Has agotado los " + str(maxNumberOfTries) + " intentos")
        break

print(userNumber) 
print(randomNumberToGuess) 
