class Solution:
    def getDecimalValue(self, head):
        v=0
        for i in head:
            v=v*2+i
        return v

res=Solution().getDecimalValue([1,1,1,1])
print(res)