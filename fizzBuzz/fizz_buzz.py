def fizzBuzz():
    listOfNumbers = []
    for number in range(1, 101):
        if ((number % 3 == 0) and (number % 5 == 0)):
            listOfNumbers.append('fizzBuzz')
        elif (number % 3 == 0):
            listOfNumbers.append('fizz')
        elif (number % 5 == 0):
            listOfNumbers.append('Buzz')
        else:
            listOfNumbers.append(number)
    return listOfNumbers

print(fizzBuzz())