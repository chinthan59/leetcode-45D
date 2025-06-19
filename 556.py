class Solution(object):
    def nextGreaterElement(self, n):
        digits = list(str(n))
        i = len(digits) - 2

        # Step 1: Find first decreasing digit from right
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i == -1:
            return -1  # No next permutation

        # Step 2: Find just larger digit on right side
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Step 3: Swap and reverse
        digits[i], digits[j] = digits[j], digits[i]
        digits[i+1:] = reversed(digits[i+1:])

        result = int(''.join(digits))
        return result if result < 2**31 else -1
