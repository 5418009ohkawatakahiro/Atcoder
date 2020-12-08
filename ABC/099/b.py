import numpy as np
a,b=map(int,input().split())
tower_h=list(np.arange(1,999+1).cumsum())
diff=b-a-1
ans=tower_h[diff]-b
print(ans)