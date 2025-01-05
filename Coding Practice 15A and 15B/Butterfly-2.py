n=int(input())

for i in range(1,n+1):
    star="* " * i
    mid_spaces ="  " * (2* (n-i))
    row= star + mid_spaces + star
    print(row)
        
for i in range(n):
    mid_spaces = "  " *((2*i))
    star="* " * (n-i)
    row=star + mid_spaces + star
    print(row)