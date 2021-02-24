n,x=map(int,input().split())
a=list(map(int,input().split()))
new_list=[]
for i in a:
    if i!=x:
        new_list.append(i)
print(*new_list)