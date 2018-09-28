squares = []
for x in range(10):
	squares.append(x**2)
print(squares)
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x*2 for x in vec])
# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])
# apply a function to all the elements
print([abs(x) for x in vec])
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])