class Solution(object):
    def majorityElement(self, nums):
        # un-allocated storage
        cand1, cand2 = None, None
        count1, count2 = 0, 0

        for num in nums: 
            # existing candidate increment
            if num == cand1: 
                count1 += 1
            elif num == cand2: 
                count2 += 1
            # candidate allocation
            elif count1 == 0: 
                cand1, count1 = num, 1
            elif count2 == 0: 
                cand2, count2 = num, 1
            # if candicates does not match, reduce count by 1
            else: 
                count1 -= 1
                count2 -= 1

        result = []
        for cand in (cand1, cand2): 
            # given statement in the question
            if cand is not None and nums.count(cand) > len(nums) // 3: 
                result.append(cand)

        return result