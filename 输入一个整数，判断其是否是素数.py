number=int(input("请输入整数m:"))
if number==1:
    print("不是素数")
elif number==2:
    print("是素数")
else:
    for i in range(2,number):
        if number%i==0:
            print("不是素数")
            break
    else:
        print("素数")
