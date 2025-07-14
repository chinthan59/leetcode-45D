class Solution:
    def increasingTriplet(self, nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

nums = [1, 2, 3, 4, 5]
res = Solution().increasingTriplet(nums)
print(res)