ls=[x for x in range(1,42)] #生成人员编号1~41的列表ls
print("依次出列的人员编号是:")
while True:
    if len(ls)<3:           #幸存者只剩两人时，中断循环
        break;
    print(ls[2],end=" ")    #输出淘汰者编号ls[2]
    ls.pop(2)               #淘汰者出列
    lt=ls[0:2]              #报数为1、2的元素，切片方式暂存
    ls.pop(0)               #报数为1、2的元素，移动到列表末尾
    ls.pop(0)
    ls.extend(lt)
print("\n幸存者编号是:")
print(ls)