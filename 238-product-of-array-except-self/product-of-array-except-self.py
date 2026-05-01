class Solution:
    def productExceptSelf(self, nums): 
        length = len(nums)
        answer = [1]*length
        # this is helping us create a list that is similler length as the given list but only contains '1'

        left_product = 1
        for i in range(length): 
            answer[i] *= left_product # answer gets multiplied with the left_product
            left_product *= nums[i] # left_product gets multiplied with the nums list in the similler index

        right_product = 1
        for i in range(length - 1, -1, -1):
            # this is going in the opposite direction starting from the end and to the 1sst
            answer[i] *= right_product # answer gets multiplied with the right_product
            right_product *= nums[i] # right_product gets multiplied with the nums list in the similler index

        return answer
        
nums = [1,2,3,4,5]
solution = Solution()
print(solution.productExceptSelf(nums))