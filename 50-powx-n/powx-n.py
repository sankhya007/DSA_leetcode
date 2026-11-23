class Solution:
    def myPow(self, x: float, n: int) -> float:
        # bruite force not working
        # if x == 0: 
        #     return 0 
        # if n == 0: 
        #     return 1

        # res = 1 
        # for i in range(abs(n)): 
        #     res *= x
        # return res if n >= 0 else 1 / res

        def helper(x, n): 
            if x == 0: 
                return 0 
            if n == 0: 
                return 1

            # square the base and have half of the exponent
            res = helper(x * x, n // 2)
            # if the exponent is odd then we are going to multiply the number one extra time with the given number itself and then return than, else we just return as is
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res