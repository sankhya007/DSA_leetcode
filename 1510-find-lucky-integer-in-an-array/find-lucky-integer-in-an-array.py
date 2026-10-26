from collections import Counter

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq = Counter(arr)

        best = -1
        for num, count in freq.items(): 
            if num == count: 
                best = max(best, num)

        return best