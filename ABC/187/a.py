ab=input().split()
a=ab[0]
b=ab[1]
a_num=0
b_num=0
for i in a:
    a_num+=int(i)
for i in b:
    b_num+=int(i)
print(max(a_num,b_num))