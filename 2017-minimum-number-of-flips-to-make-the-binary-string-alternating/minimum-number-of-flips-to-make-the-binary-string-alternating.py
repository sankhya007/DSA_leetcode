class Solution:
    def minFlips(self, s: str) -> int:

        #actual length
        n = len(s)

        # array duplicated
        s = s + s
        alt1, alt2 = [], []
        for i in range(len(s)): # using duplicated length
            # here we are going to create the alternating values for the same length of the given array which are not defective
            alt1.append("0" if i % 2 == 0 else "1") # 0101010101
            alt2.append("1" if i % 2 == 0 else "0") # 1010101010

        # using duplicate length
        res = len(s)
        diff1, diff2 = 0, 0
        left = 0 

        # running for actual length
        for right in range(len(s)): 
            # either miss-match happens, append 1 to the count
            if s[right] != alt1[right]: 
                diff1 += 1
            if s[right] != alt2[right]: 
                diff2 += 1

            if right - left + 1 > n: 
                # if missmatch meaning that is actually the wrong combination, and we are leaving that out while incrementing the window so count goes down
                if s[left] != alt1[left]: 
                    diff1 -= 1
                if s[left] != alt2[left]: 
                    diff2 -= 1
                left += 1

            if right - left + 1 == n: 
                res = min(res, diff1, diff2)

        return res
