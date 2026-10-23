class Solution(): 
    def productExceptSelf(self, nums): 

        length = len(nums)
        answer_arr = [1]*length 

        left_multiplier = 1
        for i in range(length): 
            answer_arr[i] *= left_multiplier
            left_multiplier *= nums[i]

        # now we have to go right to left 
        right_multiplier = 1
        for i in range(length-1, -1, -1): 
            answer_arr[i] *= right_multiplier
            right_multiplier *= nums[i]

        return answer_arr