"""
1:abcd
2:efgh
3:ijklmn
...
"""
f = open("data/filetest1.txt", "r")
data = f.readlines()
num = 0
for i in data:
    num += 1
    print(str(num)+":"+i,end="")

f.close()

