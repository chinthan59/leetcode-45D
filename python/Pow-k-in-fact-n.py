import math
class Solution:
    def maxKPower(self, n, k):
        fact=math.factorial(n)
        max=0
        i=0
        while i<n:
            if fact % (k**i) == 0:
                if i>max:
                    max=i
                else:
                    max=max
            i+=1
        return max

res=Solution().maxKPower(10,9)
print(res)
		        
