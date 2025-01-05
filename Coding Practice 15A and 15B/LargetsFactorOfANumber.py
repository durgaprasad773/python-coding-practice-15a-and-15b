n=int(input())
num = 0
for i in range(1,n):
    if n%i == 0:
        if i > num:
            num = i
print(num)