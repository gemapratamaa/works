firstLine = int(input())
aSet = set(input().split(' '))
thirdLine = int(input())

for i in range (1, 2*thirdLine + 1):
	targetSet = set()
	if i % 2 == 1:
		userInput = input().split(' ')
		operation = userInput[0]

	if i % 2 == 0:
		userInput = input().split(' ')
		targetSet = set(userInput)

		if operation == 'update':	
			aSet |= targetSet
		elif operation == 'intersection_update':
			aSet &= targetSet
		elif operation == 'symmetric_difference_update':
			aSet ^= targetSet
		elif operation == 'difference_update':
			aSet -= targetSet

sum = 0
listed = list(aSet)

for num in listed:
	sum += int(num)

print(sum)