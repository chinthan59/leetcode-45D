class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                lempty=(i==0 or flowerbed[i-1] == 0)
                rempty=(flowerbed[i+1] == 0 or i == len(flowerbed)-1)
                if lempty and rempty:
                    flowerbed[i] = 1
                    n -= 1
        if n <= 0:
            return True
        else:
            return False
            
res = Solution().canPlaceFlowers([1,0,0,0,1], 1)
print(res)