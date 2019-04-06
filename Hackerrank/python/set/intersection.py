firstInputNumber = int(input())
firstInput = input().split(' ')
for i in range(0, len(firstInput)):
	firstInput[i] = int(firstInput[i])

secondInputNumber = int(input())
secondInput = input().split(' ')
for i in range(0, len(secondInput)):
	secondInput[i] = int(secondInput[i])

firstSet = set(firstInput)
secondSet = set(secondInput)

intersection = firstSet.intersection(secondSet)

print(len(intersection))