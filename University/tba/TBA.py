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
# GENERATE KLEENE STAR AB & 01
#========================================================
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
    
print("{0,1}* ")
print(kleenestar01)
print("")
print("{a,b}* ")
print(kleenestarAB)
print("")

for w in kleenestarAB:
    if len(w) % 2 == 1:
        x = len(w) // 2 + 1
        if w[x - 1 : x] == 'a':
            print(w)


"""

#==================================================================================
# L1: {w  {a, b}* : #a(w) kelipatan 3 (termasuk 0) dan #b(w) tidak habis dibagi 3}.
#==================================================================================
for s in kleenestarAB:
    if s.count('a') % 3 == 0 and s.count('b') % 3 != 0:
        L1.append(s)
print("===================================================================")
print("L1: ")
L1.sort()
L1.sort(key = len, reverse = False)
print(L1)
#print(L1[0:10])
print("===================================================================")






#========================================================
# L2: {anbm : m <= 2n <= 3m, dan n, m >= 0}.
#========================================================
for a in range(0, 22):
    for b in range(0, 22):
        if b <= 2*a and 2*a <= 3*b:
            L2.append("a"*a + "b"*b)

print("L2: ")
L2.sort()
L2.sort(key = len, reverse = False)
print(L2)
#print(L2[0:10])
print("===================================================================")





#========================================================
# L3: aibjck: (i + k + 2) = j
#========================================================
for a in range (0, 8):
    for b in range (0, 8):
        for c in range (0, 8):
            if a + c + 2 == b:
                L3.append("a"*a + "b"*b + "c"*c)
L3.sort()
L3.sort(key = len, reverse = False)
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

L4.sort()
L4.sort(key = len, reverse = False)
print("L4: ") 
print(L4)
#print(L4[0:10])
print("==================================================================")






#========================================================
# L5 = {w e {0, 1}* : w tidak mengandung 1001 dan |w| > 2}.
#========================================================
for s in kleenestar01:
    if len(s) > 2 and '1001' not in s:
        L5.append(s)

L5.sort()
L5.sort(key = len, reverse = False)
print("L5: ")
print(L5)
#print(L5[0:10])
print("==================================================================")



#========================================================
# L6 = {w {0, 1}* : setiap 00 dalam w segera diikuti oleh 111}.
#========================================================
for s in kleenestar01:
    if '00' not in s:
        L6.append(s)
    if '00111' in s:
        L6.append(s)

L6.sort()
L6.sort(key = len, reverse = False)
print("L6:")
print(L6)
#print(L6[0:10])
print("==================================================================")




#========================================================
# L7 = {w e {a, b}* : w berisi substring abb dalam jumlah ganjil}.
#========================================================
for s in kleenestarAB:
    if s.count('abb') % 2 == 1:
        L7.append(s)

L7.sort()
L7.sort(key = len, reverse = False)
print("L7:")
print(L7)
#print(L7[0:10])
print("==================================================================")




#========================================================
# L8:  wa bw abw
#========================================================

L8 = []
L8.append('')
for i in range (0, 20):
    L8.append(L8[i] + 'a')
    L8.append('b' + L8[i])
    L8.append('ab' + L8[i])

listed = list(set(L8))
listed.sort()
listed.sort(key = len)
print("LISTED L8: ")
print(listed)

print("========================================================")
#========================================================
# L9: awb awbb
#========================================================
L9 = []
L9.append('')
for i in range (0,8):
    L9.append('a' + L9[i] + 'b')
    L9.append('a' + L9[i] + 'bb')


listed9 = list(set(L9))
listed9.sort()
listed9.sort(key=len)
print("L9:")
print(listed9)
print("========================================================")
#========================================================
# IRISAN L1 L2 L7
#========================================================
L1intersectL2 = list(set(L1) & set(L2))
L2intersectL7 = list(set(L2) & set(L7))
L1intersectL2.sort()
L2intersectL7.sort()
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
print("01. " + str(L1[0:10]))
print("02. " + str(L4[0:10]))
print("03. " + str(L6[0:10]))
print("04. " + str(L1intersectL2[0:10]))
print("05. " + str(L2intersectL7[0:10]))
print("06. " + str(listed[0:10]))
print("07. ")
print("08. ")
print("09. ")
print("10. ")
print("11. ")
print("12. ")
print("13. ")
print("14. ")
print("15. ")
print("16. Ya")
print("17. ")
print("18. ")
print("19. Tidak") 
#counterxample: L1 = {a}. L2 = {b}. (L1 L2)* = (ab)*. L1* L2* = a*b*")
print("20. ")

print("========================================================")
print("TEST REVERSI L5")
print("========================================================")
L5reversed = []
for i in range (0, len(L5)):
    L5reversed.append(L5[i][::-1])

def contains1001(x):
    for s in x:
        if '1001' in s:
            return True
    return False

print(L5reversed)
print("Contains 1001:" + str(contains1001(L5reversed)))
print("========================================================")
print("TEST L8 & L9")
print("========================================================")
def count(char1, char2, alist):
    for x in alist:
        print(char1 + ": " + str(x.count(char1)), end=", ")
        print(char2 + ": " + str(x.count(char2)))

count('a', 'b', L8)
print("========================================================")
count('a', 'b', L9)

print("========================================================")
print("TEST AAB IN L8")
print("========================================================")
def containsAAB(x):
    for s in x:
        if 'aab' in s:
            return True
    return False

print("Contains aab:" + str(containsAAB(L8)))
"""
