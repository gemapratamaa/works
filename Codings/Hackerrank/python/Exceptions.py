q = int(input())

for i in range(0, q):
    pair = input().split(" ")
    try:
        pair[0] = int(pair[0])
        pair[1] = int(pair[1])
        print(pair[0] // pair[1])
    except ZeroDivisionError as zde:
        print("Error Code:", zde)
    except ValueError as ve:
        print("Error Code:", ve)