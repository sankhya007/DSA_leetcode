class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = [] 
        for num_value, insert_position in zip(nums, index): 
            target.insert(insert_position, num_value)
        return target