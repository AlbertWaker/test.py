ls=[7,9,12,34,57,89,123,221,345,456]
print("原数据列表:",ls)
target=eval(input("请输入要查找的目标数据:"))
low,high=0,len(ls)-1
while True:
    mid=(low+high)//2
    if target==ls[mid]:
        print(True)
        break
    elif target<ls[mid]:
        high=mid-1
    else:
        low=mid+1
    if low>high:
        print(False)
        break
