# 某书店同本书的售书策略：如果有会员卡，购书5本(含5本)以上，书款按7.5折计算，5
# 本以下按8.5折计算；如果没有会员卡，购书5本(含5本)以上，书款按8.5折计算，5本以
# 下按9.5折计算。试写出该售书程序。
price=eval(input("请输入图书价格:"))
books=int(input("请输入购买册数:"))
flag=int(input("有会员卡，输入1，否则输入0:"))
if flag==1:
    if books>=5:
        payment=price*0.75*books
    else:
        payment=price*0.85*books
else:
    if books>=5:
        payment=price*0.85*books
    else:
        payment=price*0.95*books
print("\n您购买了价格{}元的图书{}册，付款{}元".format(price,books,payment))