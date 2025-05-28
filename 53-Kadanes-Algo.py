class Solution(object):
    def maxSubArray(self, nums):
        res=0
        curSum=0
        for n in nums:
            curSum+=n
            res=max(res,curSum)
            if curSum<0:
                curSum=0
        return res
                
nums = [-2,1,-3,4,-1,2,1,-5,4]
r=Solution().maxSubArray(nums)
print(r)