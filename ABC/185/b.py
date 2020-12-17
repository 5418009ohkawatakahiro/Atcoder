n,m,t=map(int,input().split())
ans="Yes"
battery=n
tm=0
for i in range(m):
    a,b=map(int,input().split())
    battery=battery-(a-tm)
    if battery<=0:
        ans="No"
    battery=min(battery+(b-a),n)
    tm=b
battery-=(t-tm)
if battery<=0:
    ans="No"
print(ans)