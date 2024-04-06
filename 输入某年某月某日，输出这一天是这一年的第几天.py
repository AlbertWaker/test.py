ls=[31,28,31,30,31,30,31,31,30,31,30,31]    #平年各月份天数
s=0                                         #计算总天数
year,month,day=eval(input("请输入年月日，并用逗号隔开:"))
if year%4==0 and year%100!=0 or year%400==0:
    ls[1]=29                                #若是闰年，2月份是29天
for i in range(0,month-1):                  #遍历列表前month-1个月
    s=s+ls[i]
s=s+day                                     #加上当前的日期
print("该日期是一年中的第{}天".format(s))