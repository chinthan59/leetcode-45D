class Solution(object):
    def maxSubArray(self, nums):
        res=max(nums)
        currMax,currMin=0,0
        for n in nums:
            temp=max( n + currMax,n)
            currMax=max(n + currMax,n + currMin,n)
            currMin=max(temp,n + currMin,n)
            res=max(res,currMax)
        return res
nums = [-2,1,-3,4,-1,2,1,-5,4]
r=Solution().maxSubArray(nums)
print(r)