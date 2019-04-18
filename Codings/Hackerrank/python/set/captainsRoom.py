size = int(input())

rooms = input().split(' ')
rooms.sort()

aSet = set(rooms)

for el in aSet:
	if rooms.count(el) == 1:
		print(el)

# THE TESTCASES ARE VERY STUPID ALL EXCEPT 2 OF THEM GOT TIMEOUT LIMIT