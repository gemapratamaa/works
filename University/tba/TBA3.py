
kleenestarAB = []
kleenestar01 = []
def generateKleeneStar01(s, digitsLeft):
    if digitsLeft == 0:
        kleenestar01.append(s)
        kleenestarAB.append(s)
    else:
        generateKleeneStar01(s + '0', digitsLeft - 1)
        generateKleeneStar01(s + '1', digitsLeft - 1)

for i in range (0, 8):
    generateKleeneStar01("", i)

for i in range (0, len(kleenestarAB)):
    kleenestarAB[i] = kleenestarAB[i].replace('0','a')
    kleenestarAB[i] = kleenestarAB[i].replace('1','b')
    
kleenestarAB.sort()
kleenestarAB.sort(key = len)

f = open("abNew.txt", "w")
for x in kleenestarAB:
	f.write(x + "\n")
	print(x)