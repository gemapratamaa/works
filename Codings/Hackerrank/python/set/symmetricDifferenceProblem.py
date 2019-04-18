firstInputNumber = int(input())
firstInput = input().split(' ')
for i in range(0, len(firstInput)):
	firstInput[i] = int(firstInput[i])
#print(firstInput)

secondInputNumber = int(input())
secondInput = input().split(' ')
for i in range(0, len(secondInput)):
	secondInput[i] = int(secondInput[i])
# print(secondInput)

firstSet = set(firstInput)
secondSet = set(secondInput)

symDifference = firstSet.symmetric_difference(secondSet)

listSymDifference = list(symDifference)
listSymDifference.sort()

for num in listSymDifference:
	print(num)