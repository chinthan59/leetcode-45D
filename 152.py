class Solution(object):
    def maxProduct(self, nums):
        res=max(nums)
        curMax,curMin=1,1
        for n in nums:
            if n==0:
                curMax,curMin=1,1
                continue
            temp=curMax*n
            curMax=max(n*curMax,n*curMin,n)
            curMin=min(n*curMax,n*curMin,n)
            res=max(res,curMax)
        return res
    
nums = [8,5,-1,9,0]
prod=Solution().maxProduct(nums)
print(prod)
        