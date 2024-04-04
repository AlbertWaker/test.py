#公式:Π/4≈1-1/3+1/5-1/7+...
import math
s=1.0   #表示正负号
n=1.0   #表示分母
t=1.0   #表示每个分数
pi=0.0  #表示和值
while math.fabs(t)>=1e-6:#累加到最后一项小于10的-6次方
    pi+=t
    n+=2
    s=-s
    t=s/n
pi*=4
print("PI={}".format(pi))