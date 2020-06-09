fruits = {"banana","banana","orange","apple","banana","apple","pineapple"}

print(fruits)

# print(dir(fruits))

fruits.add("pear")

print(fruits)

"""
friend = set("joaquim")
>>> {'j','o','a','q','u','i','m'}
"""

friends = set()
friends.add("auxilia")
friends.add("angelina")
friends.add("auxilia")
friends.add("rivaldo")
friends.add("serafina")

print(friends)
# print(sorted(friends))

print(50*"=")

a = {1,3,5,7,9}
b = {2,4,6,8,10}
c = {2,3,5,7,9}

t = a,b,c,
print(t)

print(a.union(b))
print(a.union(c))
print(a.intersection(b))
print(a.intersection(c))