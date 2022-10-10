numbers = [2, 4, 6, 3, 4]

numbers.sort()
n = set(numbers)
'''
for i in range(numbers):
	if numbers[i] == numbers[i+1]:
		numbers.pop(numbers[i])

for i in numbers:
	if numbers.count(i) > 1:
		numbers.remove(i)
'''

print(n)
