n,m = map(int,input().split())
num = list(map(int, input().split()))
def ret(n,num):
    for i in range(n):
        for j in range(i+1,n):
            if num[i]*num[j] == m:
                return True
    return False

r= ret(n,num)
if r:
    print("YES")
else:
    print("NO")
    
    