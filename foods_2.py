my_foods=['pizza','falafel','carrot cake']
for food in my_foods:
	print("I like pepperoni",food)
print("I really love pizzal!")
you_foods=my_foods[:]
my_foods.append('cakes')
you_foods.append('jeech')
print("My favorite pizzas are:")
for x in my_foods:
	print(x)
print("\nMy friend`s favorite pizzas are:")
for xi in you_foods:
	print(xi)
