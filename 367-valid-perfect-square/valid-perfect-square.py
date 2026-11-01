class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0 
        high = num 
        while low <= high: 
            mid = low + (high - low) // 2
            square = mid * mid # if we do match the target then we return the target
            if square == num: 
                return True
            if square < num: # we need the square to e bigger, and for that we need the mid to be bigger and to do that in an sorted array the left has to be up 
                low = mid + 1
            else:
                high = mid - 1
        return False

