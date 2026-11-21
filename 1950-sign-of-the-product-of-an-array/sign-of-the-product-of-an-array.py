class Solution:
    def arraySign(self, nums: list[int]) -> int:
        sign = 1 # let's just say that the sign is actually positive
         
        for num in nums: 
            if num == 0: 
                return 0 # it just becomes zero, because zero is getting multiplied with allf the values there are so it will be zero ne matter what
            elif num < 0: # so here what ever the fuck we have in the sign will be multiplied with the "-1" and that will change the sign, if it was positive to begin with it becomes negitive and if it was negitive it becomes positive
                sign *= -1

        return sign