from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        return [number for number, count in freq.items() if count == 2]
        