class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start, end = min(nums), max(nums)
        array = []
        for num in range(start, end + 1): 
            if num not in nums: 
                array.append(num)
        return array