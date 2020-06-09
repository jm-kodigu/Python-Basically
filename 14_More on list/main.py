animals = ["cow","elephant","wolf","tiger","cow","pig"]

print(animals)

animals.append("lion") # equals -> animals[len(animals):] = ["lion"]

animals.extend("dog") # equals -> animals[len(animals):] = "dog"

animals.insert(2,"giraffe") # or equals append() method -> animals.insert(len(animals), "giraffe")

print(animals)

animals.remove("tiger")

animals.pop()

# animals.clear() --> remove all items in list || equals del animals[:]

print(animals)

print(animals.index("lion")) # lion in position 6

t = animals.count("cow")

print("cow total is", t)

print(animals)

animals.sort()

print(animals)

animals.reverse()

print(animals)

print(40*"=")

x = animals.copy() # or equals x = animals[:]
x.append("snake")

print(animals)
print(x)