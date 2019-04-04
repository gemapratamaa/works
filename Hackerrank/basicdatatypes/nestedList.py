#still failed
firstNumber = int(input())
names = []
namesDummy = []
scoreDummy = []
scores = []
for i in range(1, 2 * firstNumber + 1):
	if i % 2 == 1:
		name = input()
		names.append(name)
	else:
		score = float(input())
		scores.append(score)
		scoreDummy.append(score)

scoreDummy.sort(reverse = True)
print(scoreDummy)
scoreDummyUnique = list(set(scoreDummy))
lowest2nd = scoreDummyUnique[1]

indexes = []

for i in range(0, len(scores)):
	if scores[i] == lowest2nd:
		indexes.append(i)
		scores[i] = 9999999
		namesDummy.append(names[i])

#print(indexes)

namesDummy.sort()
for name in namesDummy:
	print(name)