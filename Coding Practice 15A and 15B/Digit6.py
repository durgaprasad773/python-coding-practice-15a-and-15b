n=int(input())

for i in range(1,2*n):
    if i==1 or i==n or (i==((2*n)-1)):
        print("* " * n)
    elif i<n:
        print("* ")
    else:
        hollow="  " * (n-2)
        row="* " + hollow +"*"
        print(row)
        