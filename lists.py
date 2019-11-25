demo_list = [1, 'hello', 1.34, True, [1,2,3]]

colors= ['red', 'green', 'blue']

number_list = list((1,2,3,4))

print(number_list)

print(list(range(1, 100)))

print(colors[1])

print('greenu' in colors)

colors[1] = 'pedru'

print(colors[1])
#append solo permite añadir de uno en uno
colors.append('moradu')
#para añadir más
colors.extend(['violetu','yellou'])
colors.extend(['pinku','blacku'])

colors.insert(len(colors), 'moradu')

print(colors)

colors.pop()
print(colors)

colors.remove('blue')
print(colors)

colors.clear()
print(colors)
