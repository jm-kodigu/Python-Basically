import sys,timeit

hello = ("terezinha","elia","basilio","donacio","januario")

print(hello[0])
print(hello[3])
print(hello.index("elia"))
print(hello.count("basilio"))

hi = ("joaquim","licenia","luduvina","marciana")

t = hello, hi

print(t)

print(t[0][4],t[1][0])

print(30*"==")

date_list = ["jmkodigu","python",17,12.7,True]
date_tuple = ("jmkodigu","python",17,12.7,True)

print("size of list", sys.getsizeof(date_list))
print("size of tuple", sys.getsizeof(date_tuple))

print(60*"=")

a = timeit.timeit(number=1000000,stmt='["jmkodigu","python",17,12.7,True]')
b = timeit.timeit(number=1000000,stmt='("jmkodigu","python",17,12.7,True)')

print("list time :", a)
print("tuple time :", b)