class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        counter = 0
        for act, exp in zip(heights, expected): 
            if act != exp: 
                counter += 1 
        
        return counter
