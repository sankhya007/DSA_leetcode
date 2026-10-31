class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        open = 0 
        close = 0

        for ch in s: 
            if ch == "(": 
                open += 1
            elif open: # ch is closing, but there is an unpached openning before it so the counter goes down
                open -= 1
            else: # closing without any openning before, so the counter for closing goes up 
                close += 1

        return open + close