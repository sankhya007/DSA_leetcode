class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None 
        # ths is None because if it was 0, it could have also been a candidate in the given list

        for num in nums: 
            if count == 0: 
                candidate = num #if the count hits 0 then the candidate can change or else the count just does down by 1
            count += (1 if candidate == num else -1)
            # if the number matches then the count goes up or else down

        return candidate

nums = [2,2,1,1,1,2,2]
solution = Solution()
print(solution.majorityElement(nums))