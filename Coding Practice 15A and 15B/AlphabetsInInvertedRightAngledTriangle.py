n=int(input())

for i in range(n):
    num = 65
    row=""
    for j in range(n-i):
        row = row + chr(num)+" "
        num+=1
    print(row)