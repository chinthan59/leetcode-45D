class Solution(object):
    def reverseString(self, s):
        for i in range(len(s)//2):
            s[i],s[len(s)-(i+1)]= s[len(s)-(i+1)],s[i]
        return s
s = ["h", "e", "l", "l", "o","w"]
res = Solution().reverseString(s)
print(res)