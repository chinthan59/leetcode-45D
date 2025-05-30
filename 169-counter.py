from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        nums=Counter(nums)
        return max(nums, key=nums.get)
nums = [3,2,3,2]
res=Solution().majorityElement(nums)
print(res)

#not efficient