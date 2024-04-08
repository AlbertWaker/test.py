import random
def hongbao(cash,n):
    global count
    while True:
        t=random.uniform(0.01,cash-0.01*n)
        t=round(t,2)
        if count<n-1:
            d[ls[count]]=t
            cash=cash-t
            count=count+1
        else:
            d[ls[count]]=round(cash,2)
            count=count+1
            break
member=["Lucy","Jerry","Mike","Jack","Tom","Rose","White","Jim"]
print("目前群中共有{}人:".format(len(member)),end=" ")
for i in member:#输出目前群中人员列表
    print(i,end=" ")
print()
total=eval(input("输入红包总金额:"))
num=eval(input("输入红包个数:"))
count=0#全局变量，用来统计已发红包个数
ls=random.sample(member,num)#从微信成员中随机生成领取红包人员列表，全局变量
d={}#全局变量，字典d，用于记录红包发放情况
hongbao(total,num)
for i in d:
    print("{}领取{}元".format(i,d[i]))
t=max(d.items(),key=lambda x:x[1])#依据红包金额，提取字典最大元素
print("一共有{}人领取了红包，手气最佳{}，领取{}元".format(count,t[0],t[1]))
