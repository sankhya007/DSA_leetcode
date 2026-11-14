class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        sort = sorted(heights)
        i = count = 0 

        while i < len(heights):
            if heights[i] != sort[i]: 
                count += 1
            i += 1

        return count