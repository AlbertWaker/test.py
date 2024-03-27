a=float(input("请输入三角形的边长a:"))
b=float(input("请输入三角形的边长b:"))
c=float(input("请输入三角形的边长c:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("三角形面积为:",area)
