s=input("请输入一行英文文本:")
for ch in s:
    if ch in "~!@#$%^&*()_+|}{:\"<>?;,.\'/":
        s=s.replace(ch," ")
s=s.strip()
ls=s.split()
print("单词个数={}".format(len(ls)))
