"""
numbers =  [5,2,1,5,7,4]
numbers2 = numbers.copy()
numbers.append(10)

print(numbers2)

"""

#Challenge
"""
numbers = [5,2,3,8,2,1,1,8]
duplicate =numbers[0]
for value in numbers:
    if numbers.count(value) > 1:
        numbers.remove(value)
print(numbers)
"""
numbers = [5,2,3,8,2,1,1,8]
unique =[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)



