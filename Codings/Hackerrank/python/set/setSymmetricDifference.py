firstInputNumber = int(input())
firstInput = input().split(' ')
#print(firstInput)

secondInputNumber = int(input())
secondInput = input().split(' ')
# print(secondInput)

firstSet = set(firstInput)
secondSet = set(secondInput)

difference = firstSet.symmetric_difference(secondSet)
print(len(difference))