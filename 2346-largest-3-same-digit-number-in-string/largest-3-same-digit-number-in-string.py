# from collections import Counter

# class Solution:
#     def largestGoodInteger(self, num: str) -> str:
#         freq = Counter(num)
#         max_value = ""

#         for digit, value in freq.items(): 
#             if value >= 3: 
#                 max_value = max(max_value, digit*3)               

#         return max_value

# will not work because will also count the values which are not sitting along side of each otehr 

class Solution:
    def largestGoodInteger(self, num: str) -> str:

        best = ""

        for i in range(len(num) - 2): 
            if num[i] == num[i + 1] == num[i + 2]: 
                best = max(best, num[i] *3)

        return best