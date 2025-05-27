class Solution(object):
    def sortedSquares(self, nums):
        for i in range(0,len(nums)):
            nums[i]=nums[i]**2
        return sorted(nums)

nums=[-7,-3,2,3,11]
res=Solution().sortedSquares(nums)
print(res)