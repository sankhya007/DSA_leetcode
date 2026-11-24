class Solution:
    def minMoves(self, nums: List[int]) -> int:
        to_match = max(nums)
        total = 0 
        for num in nums: 
            total += to_match - num
        return total
