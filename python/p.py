class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = []
        i = j = 0
        n, m = len(word1), len(word2)

        while i < n or j < m:
            if i < n:
                merged.append(word1[i])
                i += 1
            if j < m:
                merged.append(word2[j])
                j += 1

        return ''.join(merged)

res = Solution().mergeAlternately('abc','pqr')
print(res)