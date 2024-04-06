n=eval(input("请输入加密密钥:"))
txt=input("请输入原文:")
newtxt=""
for ch in txt:
    if 'a'<=ch<='z':
        s=chr(ord('a')+(ord(ch)+n-ord('a'))%26)
    elif 'A'<=ch<='Z':
        s=chr(ord('A')+(ord(ch)+n-ord('A'))%26)
    else:
        s=ch
    newtxt=newtxt+s
print("密文是:",newtxt)