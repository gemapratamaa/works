T = int(input())
setA = []
setB = []

def isSubset(a, b):
	aList = list(a)
	bList = list(b)

	for element in aList:
		if element not in bList:
			return False

	return True


for i in range(1, 4*T + 1):
	userInput = input()
	
	if i % 4 == 2:
		setA = userInput.split(" ")
		#print("SET A: " + str(setA))

	if i % 4 == 0:
		setB = userInput.split(" ")
		#print("SET B: " + str(setB))
		print(isSubset(setA, setB))
		setA.clear()
		setB.clear()