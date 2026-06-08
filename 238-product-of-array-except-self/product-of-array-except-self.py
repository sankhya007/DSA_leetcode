class Solution(): 
    def productExceptSelf(self, nums): 
        length = len(nums)
        answer = [1]*length
        left_multiplier = 1
        for i in range(length): 
            answer[i] *= left_multiplier
            left_multiplier *= nums[i]
        right_multiplier = 1
        for i in range(length-1, -1, -1): 
            answer[i] *= right_multiplier
            right_multiplier *= nums[i]
        return answer