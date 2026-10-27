from collections import defaultdict

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        seen = defaultdict(int)

        for word in words: 
            for c in word: 
                seen[c] += 1
        # increment everytime it is seen

        for c in seen:
            if seen[c] % len(words): 
                return False
        # the len of array is the ideal len if every string

        return True