class Solution:
    def largestGoodInteger(self, num: str) -> str:

        current_num = max_num = ""
        for i in range(len(num)-2): 
            if num[i] == num[i+1] == num[i+2]: 
                current_num = num[i] + num[i+1] + num[i+2]
                max_num = max(current_num, max_num)

        return max_num
