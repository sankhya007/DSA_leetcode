class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        storage = {}

        for i, num in enumerate(nums): 
            if target - num in storage: 
                return [storage[target - num], i]

            storage[num] = i