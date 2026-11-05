class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        current_cost = 0 
        left = 0 
        res = 0 

        for right in range(len(s)): 
            current_cost += abs(ord(s[right]) - ord(t[right]))
            while current_cost > maxCost: 
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            # window size because that is the ammount of eleemts that we can change in the given circumstance
            res = max(res, right - left + 1)

        return res