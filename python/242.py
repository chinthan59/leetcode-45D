class Solution(object):
    def isAnagram(self, s, t):
        if sorted(t)==sorted(s):
            return True
        else:
            return False

res=Solution().isAnagram(s, t)
print(res)