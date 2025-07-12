class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        h = max(candies)
        return [c + extraCandies >= h for c in candies]
    
res = Solution().kidsWithCandies([4,2,1,1,2], 1)
print(res)