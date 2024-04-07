def Fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return Fib(n-2)+Fib(n-1)
for i in range(1,21):
    print(Fib(i),end=" ")
