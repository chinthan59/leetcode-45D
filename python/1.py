class Solution(object):
    def twoSum(self, nums, target):
        d=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    d.append(i)
                    d.append(j)
        return d
nums = [2,7,11,15]
res=Solution().twoSum(nums, 18)
print(res)
