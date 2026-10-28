class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # rank = {c:i for i, c in enumerate(order)}
        # return ''.join(sorted(s, key=lambda c: rank.get(c, 26)))

        count = [0] * 26
        for c in s: 
            count[ord(c) - ord('a')] += 1 

        res = []
        for c in order: 
            index = ord(c) - ord('a')
            while count[index]: 
                res.append(c)
                count[index] -= 1

        for index in range(26): 
            c = chr(ord('a') + index)
            while count[index]: 
                count[index] -= 1
                res.append(c)

        return ''.join(res)