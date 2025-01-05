n=int(input())


for i in range(1,n+1):
    row=""
    num = 65
    for j in range(1,n+1):
        row = row + chr(num)+" "
        num+=1
    print(row)