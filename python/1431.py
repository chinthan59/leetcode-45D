class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        h = max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=h:
                res.append(True)
            else:
                res.append(False)
        return res
    
res = Solution().kidsWithCandies([4,2,1,1,2], 1)
print(res)