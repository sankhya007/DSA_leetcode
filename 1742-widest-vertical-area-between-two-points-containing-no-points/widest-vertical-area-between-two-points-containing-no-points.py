class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort()
        difference, max_difference = 0, 0
        for i in range(1, len(points)):
            difference = points[i][0] - points[i-1][0]
            max_difference = max(difference, max_difference)
        return max_difference
            
