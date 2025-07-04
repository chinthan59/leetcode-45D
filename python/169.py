from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        res,count=0,0
        for n in nums:
            if count==0:
                res=n
            count+=1 if n==res else -1
        return res
        
nums = [3,2,3,3,3,2,2]
res=Solution().majorityElement(nums)
print(res)