def div_step(m,n):
    st=0
    st=(m-(m%n))//n
    print("steps:",st)
    print("remainder:",m%n)

res=div_step(12,3)
print(res)