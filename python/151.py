class Solution(object):
    def reverseWords(self, s):
        w = s.split()
        return " ".join(w[::-1])  

s = "the sky is blue"
res = Solution().reverseWords(s)
print(res)
