def fizzBuzz():
    listOfNumbers = [1,2]
    for number in range(1, 100):
        if ((number % 3 == 0) and (number % 5 == 0)):
            listOfNumbers.append('fizzBuzz')
        elif (number % 3 == 0):
            listOfNumbers.append('fizz')
        elif (number % 5 == 0):
            listOfNumbers.append('Buzz')
    return listOfNumbers

print(fizzBuzz())