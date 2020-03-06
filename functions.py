def hello(name="Person"):
    print('Hello ' + name)

hello("Joe");
hello("Ryan");

hello();

def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(10, 30))
print(add(1000, 3980))

##lambda
addLambda = lambda number1, number2: number1 + number2

print(addLambda(111,30))