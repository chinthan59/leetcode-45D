class Solution(object):
    def reverseVowels(self, s):
        p=[i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        v = [l for l in s if l in 'aeiouAEIOU']
        v.reverse()
        k=0
        for i in p:
            s=s[:i]+v[k]+s[i+1:]
            k += 1
        return s
s="leetcode"
res = Solution().reverseVowels(s)
print(res)