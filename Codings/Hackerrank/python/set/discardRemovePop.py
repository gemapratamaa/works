numOfElements = int(input())

dummyList = input().split(' ')
realSet = set()

for num in dummyList:
	realSet.add(int(num))

commands = int(input())

for i in range(0, commands):
	userInput = input().split(' ')

	if userInput[0] == 'pop':
		realSet.pop()
	elif userInput[0] == 'remove':
		target = int(userInput[1])
		realSet.remove(target)
	elif userInput[0] == 'discard':
		target = int(userInput[1])
		realSet.discard(target)

listed = list(realSet)

sum = 0
for element in listed:
	sum += element

print(sum)