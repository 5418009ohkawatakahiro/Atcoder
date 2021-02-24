s=input()
s_odd=s[0::2]
s_even=s[1::2]
ans="No"
if s_odd.islower()==True and (s_even.isupper()==True or len(s_even)==0):
    ans="Yes"
print(ans)