# two sum

class Solution(): 
    def twoSum(self, nums, target): 
        storage = {}

        for i, num in enumerate(nums): 
            left_over = target - num

            # return left_over location, rather than value
            if left_over in storage: 
                return [storage[left_over], i]

            # store location in left_over's value location
            storage[num] = i