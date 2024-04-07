def prime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True
count=0
for j in range(100,201):
    if prime(j):
        print(j,end=" ")
        count+=1
print("\n100~200之间素数的个数:",count)
