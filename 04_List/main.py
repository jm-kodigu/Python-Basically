numbers = [1,3,19,89,100]

print(numbers)

print(10*'=')

print(numbers[0])
print(numbers[4])
print(numbers[-1])
print(numbers[-3:])
print(numbers[:])

numbers[2] = 80

print(numbers)

# add new items at the end of list with append() methods
numbers.append(12)
numbers.append(74//3)

print(numbers)

print(30*'=')

alphabet = ['A','B','C','D','E','F']
print(alphabet)
alphabet[1:4] = ['Z','Y','W']
print(alphabet)
alphabet[2:5] = []
print(alphabet)
alphabet[:] = []
print(alphabet)

world = ["python","java","html & css","javascript"]
print(len(world))

fruits = ["grape","apple","pineapple","watermelon"]
items = ["doll","soap","knife","fork"]

"""
all_items = fruits + items

print(all_items)
"""

# list contain other list
all_items = [fruits,items]

print(all_items)

print(all_items[0][1])
print(all_items[1][2])
print(all_items[1][1:3])
all_items[0][0] = "papaya"
all_items[1][2:] = ["spoon","plate"]
print(all_items)

all_items[:] = []

print(all_items)

a = [100,330,0.3,32]
print(a)
# b = a.copy()
b = a[:]
print(b)
b.append('ju' 'liao')
b.append(True)
print("b =", b)
print("a =", a)