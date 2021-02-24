h,w=map(int,input().split())
s=[]
ans=0
for _ in range(h):
    s_i=input()
    s.append(s_i)
for i in range(len(s)-1):
    for j in range(len(s[i])-1):
        cnt=0
        if s[i][j]=="#":
            cnt+=1
        if s[i+1][j]=="#":
            cnt+=1
        if s[i][j+1]=="#":
            cnt+=1