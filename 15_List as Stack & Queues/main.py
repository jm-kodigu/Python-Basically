print("List as Stack!\n")

nums = [1,2,3]
print(nums)

nums.append(4)
print(nums)

nums.append(5)
nums.append(6)
nums.append(7)
print(nums)

nums.pop()
print(nums)
nums.pop()
print(nums)
nums.pop()
nums.pop()
nums.pop()
print(nums)

print('\n',20*"=",'\n')

print("List as Queues!\n")

from collections import deque

number = deque([1,2,3,4])
print(number)

number.append(5)
number.append(6)

print(number)

number.popleft()

print(number)

number.popleft()

print(number)

number.popleft()
number.popleft()

print(number)