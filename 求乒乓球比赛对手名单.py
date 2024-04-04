# #两支乒乓球队进行比赛，各出三人。甲队为a、b、c三人，乙队为x、y、z三人。以抽签决定
# 比赛名单。有人向队友打听比赛的名单，a说他不和x比，c说他不和x、y比。编写程序找出三
# 场比赛对手的名单。
for i in "xyz":
    for j in "xyz":
        if i!=j:
            for k in "xyz":
                if(i!=k)and(j!=k):
                    if(i!="x")and(k!="x")and(k!="y"):
                        print("对战顺序是:\na--{}\nb--{}\nc--{}\n".format(i,j,k))