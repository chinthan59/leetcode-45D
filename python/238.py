import math
class Solution(object):
    def productExceptSelf(self, nums):
        l=[]
        nl=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    l.append(nums[j])
            nl.append(math.prod(l))
            l.clear()
        return nl
s = [1,2,3,4]
res = Solution().productExceptSelf(s)
print(res)