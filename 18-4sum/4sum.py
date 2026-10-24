class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        nums.sort()
        length = len(nums)
        quads = []

        for i in range(length - 3): 
            if i > 0 and nums[i] == nums[i - 1]: 
                continue

            for j in range(i + 1, length - 2): 
                if j > i + 1 and nums[j] == nums[j - 1]: 
                    continue 

                left = j + 1 
                right = length - 1

                while left < right: 

                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum == target: 
                        quads.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1 
                        right -= 1 

                        while left < right and nums[left] == nums[left - 1]: 
                            left += 1 

                        while left < right and nums[right] == nums[right + 1]: 
                            right -= 1

                    elif current_sum < target: 
                        left += 1

                    else: 
                        right -= 1

        return quads