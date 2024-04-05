a=[x for x in range(1,10)]
b=[y for y in range(1,10)]
c=[(y,x,x*y) for x in a for y in b if y<=x]
for i in c:
    print("{}*{}={}".format(i[0],i[1],i[2]),end="\t")
    if i[0]==i[1]:
        print()