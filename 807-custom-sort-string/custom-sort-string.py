# class Solution:
#     def customSortString(self, order: str, s: str) -> str:

#         string = "" 

#         for ch in order: 
#             if ch in s: 
#                 string += ch
#             else: 
#                 continue

#         for ch in s: 
#             if ch not in string: 
#                 string += ch
#             else: 
#                 continue

#         return string


class Solution:
    def customSortString(self, order: str, s: str) -> str:

        count = [0] * 26
        for c in s: 
            count[ord(c) - ord('a')] += 1
        # this portion is assigning the values that we have and also counting down the dupes

        res = []
        for c in order: 
            # get the specific index of the letter that we have in order
            index = ord(c) - ord('a')
            while count[index]: 
                # res will append that character and form the main index the count will be dicked down
                res.append(c)
                count[index] -= 1

        for index in range(26): 
            c = chr(ord('a') + index) # so c can be a to z
            while count[index]: # while there are values in that count meaning the onces that have 0 will not count but anything more than 0 will count and also if the number is more than 1 it will be pasted that many times only
                count[index] -= 1
                res.append(c)

        # array to one string format
        return ''.join(res)