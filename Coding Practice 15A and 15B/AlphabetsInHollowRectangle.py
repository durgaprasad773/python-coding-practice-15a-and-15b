m=int(input())
n=int(input())
num = 65

for i in range(1,m+1):
    if i==1 or i==m:
        row=""
        for j in range(1,n+1):
            row = row + chr(num)+" "
            num += 1
        print(row)
    else:
        row=""
        hollow="  " * (n-2)
        lenght = (len(hollow)//2)+1
        row = row + chr(num) +" "+ hollow 
        num = num + lenght
        row += chr(num)
        num = num + 1
        print(row)