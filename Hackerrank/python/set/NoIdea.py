firstLine = input().split(' ')

n = firstLine[0]
m = firstLine[1]

array = input().split(' ')

setA = set(input().split(' '))
setB = set(input().split(' '))

happiness = 0

for num in array:
	if num in setA:
		happiness += 1
	if num in setB:
		happiness -= 1

print(happiness)