class Solution(object):
    def majorityElement(self,nums):
        if not nums:
            return []

    # Step 1: Find possible candidates
        count1, count2, candidate1, candidate2 = 0, 0, None, None

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

    # Step 2: Validate the candidates
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums) // 3:
                result.append(c)

        return result

nums = [3,2,3,3,3,2,2]
res=Solution().majorityElement(nums)
print(res)