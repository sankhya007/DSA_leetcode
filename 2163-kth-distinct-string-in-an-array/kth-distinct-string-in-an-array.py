from collections import Counter
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        # count frequency
        freq = Counter(arr)

        for s in arr: 
            # if one, counter go down by 1
            if freq[s] == 1: 
                k -= 1
                # when hit zero we get answer
                if k == 0: 
                    return s

        return ""