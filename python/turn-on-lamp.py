n=10
l,il=2,8
def lamp(n, l,il):
    lamps = [0] * (n+1)
    lamps[l]+=1
    lamps[il+1]-=1
    for i in range(1, n+1):
        lamps[i] += lamps[i-1]
    return lamps[1:n+1]

res=lamp(n, l, il)
print(res)