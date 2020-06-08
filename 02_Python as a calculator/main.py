# using python as a calculator

"""
the operators

+ -> addition
- -> subtration
* -> multiplication
/ -> division

() -> parentheses can be use for grouping

"""

print(2 + 8)
print(30 - 4)
print(5 * 3)
print(9 / 3) # result 3.0, division always return a floating point number
print((10 + 2) * 3)

"""
the integer number

(e.g. 1,30,100,-2) have type int
(e.g. 8.10,1.6,-20.1) have type float

"""

# division always return a floating to get a integer, use // -> floor division

print(9 // 3) # result 3 have type int

# to calculate the remainder you can use %
print(10 % 3)
print(8 % 5)

# operator exponent ** operator to calculate the powers
print(5**2)
print(2**7)

# the equals use to assign a value to variable.
apple = 3
grape = 10 * 2

print(apple + grape)

# use python to calculate math score
# get score
exercise = 79
homework = 98
exame = 65

# index
print("exercise =", exercise)
print("homework =", homework)
print("exame =", exame)
# total score get
mathscore_total = (exercise + homework + exame) // 3

print("math score total is", mathscore_total)