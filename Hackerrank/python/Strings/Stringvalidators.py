s = input()

alnum = False
alpha = False
digit = False
upper = False
lower = False

for char in s:
	if char.isalnum():
		alnum = True
		break

for char in s:
	if char.isalpha():
		alpha = True
		break

for char in s:
	if char.isdigit():
		digit = True
		break

for char in s:
	if char.isupper():
		upper = True
		break

for char in s:
	if char.islower():
		lower = True
		break

print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)