#========================================================
# INITIALIZE EMPTY LIST
#========================================================
L1 = []
L2 = []
L3 = []
L4 = []
L5 = [] 
L6 = []
L7 = []
L8 = []
L9 = []
kleenestarAB = []
kleenestar01 = []
#========================================================
# GENERATE KLEENE STAR A B & 0 1
#========================================================
def generateKleeneStar01(s, digitsLeft):
    if digitsLeft == 0:
        kleenestar01.append(s)
        kleenestarAB.append(s)
    else:
        generateKleeneStar01(s + '0', digitsLeft - 1)
        generateKleeneStar01(s + '1', digitsLeft - 1)

for i in range (0, 5):
    generateKleeneStar01("", i)

for i in range (0, len(kleenestarAB)):
    kleenestarAB[i] = kleenestarAB[i].replace('0','a')
    kleenestarAB[i] = kleenestarAB[i].replace('1','b')
    
#print("KLEENESTAR {0,1}*: " + str(kleenestar01))
print("")
#print("KLEENESTAR {a,b}*: " + str(kleenestarAB))
print("")



#========================================================
# L1: {w  {a, b}* : #a(w) kelipatan 3 (termasuk 0) dan #b(w) tidak habis dibagi 3}.
#========================================================
for s in kleenestarAB:
    if s.count('a') % 3 == 0 and s.count('b') % 3!= 0:
        L1.append(s)
print("===================================================================")
#
print("L1: ")
print(L1)
#print(L1[0:10])
print("===================================================================")


#========================================================
# L2: {anbm : m <= 2n <= 3m, dan n, m >= 0}.
#========================================================
for a in range(0, 5):
    for b in range(0, 5):
        if b <= 2*a and 2*a <= 3*b:
            L2.append("a"*a + "b"*b)

print("L2: ")
print(L2)
#print(L2[0:10])
print("===================================================================")



#========================================================
# L3: aibjck: (i + k + 2) = j
#========================================================
for a in range (0, 6):
    for b in range (0, 6):
        for c in range (0, 6):
            if a + c + 2 == b:
                L3.append("a"*a + "b"*b + "c"*c)
print("L3: ")
print(L3)
#print(L3[0:10])
print("===================================================================")


#========================================================
# L4: ambncpdq : m+q==n+p
#========================================================
for a in range (0, 4):
    for b in range(0, 4):
        for c in range(0, 4):
            for d in range(0, 4):
                if a + d == b + c:
                    L4.append("a"*a + "b"*b + "c"*c + "d"*d)

print("L4: ") 
print(L4)
print("==================================================================")



#========================================================
# L5 = {w e {0, 1}* : w tidak mengandung 1001 dan |w| > 2}.
#========================================================
for s in kleenestar01:
    if len(s) > 2 and '1001' not in s:
        L5.append(s)
print("L5: ")
print(L5)
print("==================================================================")



#========================================================
# L6 = {w {0, 1}* : setiap 00 dalam w segera diikuti oleh 111}.
#========================================================
for s in kleenestar01:
    if '00' not in s:
        L6.append(s)
    if '00111' in s:
        L6.append(s)

print("L6:")
print(L6)
print("==================================================================")

#========================================================
# L7 = {w e {a, b}* : w berisi substring abb dalam jumlah ganjil}.
#========================================================
for s in kleenestarAB:
    if s.count('abb') % 2 == 1:
        L7.append(s)

print("L7:")
print(L7)
print("==================================================================")

#========================================================
# L8:  wa bw abw
#========================================================
L8append1 = []
L8append2 = []
L8append3 = []
L8append1.append('')
L8.append('')

for s in L8:
    L8append1.append(s + 'a')
    L8append1.append('b' + s)
    L8append1.append('ab' + s)

for s in L8append1:
    L8append2.append(s + 'a')
    L8append2.append('b' + s)
    L8append2.append('ab' + s)

for s in L8append2:
    L8append3.append(s + 'a')
    L8append3.append('b' + s)
    L8append3.append('ab' + s)

total8 = list(set().union(L8, L8append1, L8append2, L8append3))
total8.sort()
total8.sort(key = len, reverse = False)
print("L8: " + str(total8))
print("#========================================================")
#========================================================
# L9: awb awbb
#========================================================
L9append1 = []
L9append2 = []
L9append3 = []
L9append1.append('')
L9.append('')

for s in L9:
    L9append1.append('a' + s + 'b')
    L9append1.append('a' + s + 'bb')

for s in L9append1:
    L9append2.append('a' + s + 'b')
    L9append2.append('a' + s + 'bb')

for s in L9append2:
    L9append3.append('a' + s + 'b')
    L9append3.append('a' + s + 'bb')


total9 = list(set().union(L9, L9append1, L9append2, L9append3))
total9.sort()
total9.sort(key = len, reverse = False)
print("L9: " + str(total9))
print("#========================================================")
#========================================================
# IRISAN L1 L2 L7
#========================================================
L1intersectL2 = list(set(L1) & set(L2))
L2intersectL7 = list(set(L2) & set(L7))
L1intersectL2.sort(key = len, reverse = False)
L2intersectL7.sort(key = len, reverse = False)

print("L1 && L2:")
print(L1intersectL2)
print("========================================================")
print("L2 && L7:")
print(L2intersectL7)
print("========================================================")






#========================================================
print("JAWABAN AKHIR: ")
print("========================================================")
print("1. " + str(L1[0:10]))
print("2. " + str(L4[0:10]))
print("3. " + str(L6[0:10]))
print("4. " + str(L1intersectL2))
print("5. " + str(L2intersectL7[0:10]))
print("6. ")
print("7. ")
print("8. ")
print("9. ")