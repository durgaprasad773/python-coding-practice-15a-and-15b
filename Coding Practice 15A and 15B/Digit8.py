n=int(input())

for i in range(1,(2*n+2)):
    if i==1 or i==(n+1) or (i==(2*n+1)):
        print("* " * n)
    else:
        space ="  " * (n-2)
        row="* " + space +"*"
        print(row)
        