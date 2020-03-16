import pandas as pd
import numpy as np

l=input("输入与好友秘密关系为“朋友”的QQ账号，多个请用空格隔开：")
yes_list = l.split(" ")
ms=input("输入与好友秘密关系为“朋友的朋友或非朋友”的QQ账号，多个请用空格隔开：")
no_list = ms.split(" ")
df = pd.DataFrame(columns=["qq"])
count =0
if yes_list:
    for i in yes_list:
        a = []
        f = open(i+".txt").read().split("\n")
        for j in f:
            a.append(j)
        d=pd.DataFrame(np.array(a),columns=["qq"])
        if (count == 0):
            df = df.append(d)
            count=count+1
        else:
            df = pd.merge(df,d,how='inner')
if no_list:
    for i in no_list:
        b = []
        f = open(i + ".txt").read().split("\n")
        for j in f:
            b.append(j)
        d = pd.DataFrame(np.array(b), columns=["qq"])
        df = df.append(d)
        df = df.append(d)
        df = df.drop_duplicates(subset=["qq"], keep=False)
        # a与b的差集 a=a-b
print("筛选结果如下:")
for i in range(0, len(df)):
    print(df.iloc[i]['qq'])