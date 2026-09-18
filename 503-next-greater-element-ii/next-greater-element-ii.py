class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        result = [-1] * n 
        stack = []

        # run for twice the size so then it can input and then also compare
        for i in range(2 * n): 

            # compare last element with left over
            while stack and nums[stack[-1]] < nums[i % n]: 
                # store number in mentioned position 
                result[stack.pop()] = nums[i % n]

            if i < n: 
                stack.append(i)
        
        return result
