n=int(input())
dp=list(range(n+1))
for i in range(n+1):
    six=6
    while 0<=(i-six):
        dp[i]=min(dp[i],dp[i-six]+1)
        six*=6
    nine=9
    while 0<=(i-nine):
        dp[i]=min(dp[i],dp[i-nine]+1)
        nine*=9
print(dp[-1])