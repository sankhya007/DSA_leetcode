class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0 
        right = n

        while left <= right: 
            mid = left + (right - left) // 2 
            total = mid * (mid + 1) // 2 # to make up your own target
            # total is the count of coiuns that i am going to need to fill out rows till mid
            if total == n: 
                return mid
            if total < n:
                left = mid + 1
            else: 
                right = mid - 1

        return right