def isStrictSubset(a, b):
	aList = list(a)
	bList = list(b)

	if a == b:
		return False

	for element in aList:
		if element not in bList:
			return False

	return True

setA = input().split(' ')
numberOfSets = int(input())

flag = True
for i in range(0, numberOfSets):
	inputSet = input().split(' ')

	if not isStrictSubset(inputSet, setA):
		flag = False
		break

print(flag)
