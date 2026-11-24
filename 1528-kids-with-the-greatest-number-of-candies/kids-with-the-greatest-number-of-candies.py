class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        greatest = max(candies)
        ans = [False] * len(candies)
        for i, candy in enumerate(candies): 
            if candy + extraCandies >= greatest: 
                ans[i] = True
        return ans