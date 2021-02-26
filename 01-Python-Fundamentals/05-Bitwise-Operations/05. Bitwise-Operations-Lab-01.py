n = int(input())  # integer number
b = input()  # single binary digit

count = bin(n)[2:].count(b)
print(count)