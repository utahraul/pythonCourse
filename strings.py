myStr = "Hello World"

#print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("Hello", "Bye").upper())
print(myStr.count("l"))
print(myStr.count("o"))
print(myStr.count(" "))

print(myStr.startswith("Hola"))
print(myStr.startswith("Hello"))
print(myStr.endswith("World"))

print(myStr.split("o"))

print(myStr.find(" "))

print(len(myStr))

print(myStr.index("e"))

print(myStr.isnumeric())

print(myStr.isalpha())

print(myStr[0])

#Con menos delante empieza desde atras
print(myStr[-1])

name = "Raúl"
print("My name is " + name)
#De 3.6 hacía arriba
print(f"My name is {name}")
print("My name is {0}".format(name))
