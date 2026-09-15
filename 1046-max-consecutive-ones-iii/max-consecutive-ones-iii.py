# minimum size sub-array sum

class Solution(): 
    def longestOnes(self, nums, k): 

        left = 0 
        zeros = 0 
        max_length = 0 

        # right increment
        for right in range(len(nums)): 

            # count the number of zeros
            if nums[right] == 0: 
                zeros += 1 

            # make sure we leave out the extra zeros from k at the left
            while zeros > k: 
                # check if left zero 
                if nums[left] == 0:
                    # decrement zero
                    zeros -= 1 

                # left pointer moves forward
                left += 1 

            # check if the window position is making the max no of 1s 
            max_length = max(max_length, right - left + 1)

        return max_length