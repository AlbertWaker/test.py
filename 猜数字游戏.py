import random
number=random.randint(1,1000)
while True:
    guess=eval(input("输入一个整数:"))
    if guess<number:
        print("猜小了")
    elif guess>number:
        print("猜大了")
    else:
        print("猜中了")
        break