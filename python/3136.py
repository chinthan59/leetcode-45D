import re
class Solution:
    def isValid(self,word):
        if len(word)<3:
            return False
        if not word.isalnum():
            return False
        vowels = set("aeiouAEIOU")
        has_vowel = False
        has_consonant = False

        for ch in word:
            if ch.isalpha():
                if ch in vowels:
                    has_vowel=True
                else:
                    has_consonant=True
            if has_vowel and has_consonant:
                break
        return has_vowel and has_consonant
    
    
res=Solution().isValid("123@Abc")
print(res)