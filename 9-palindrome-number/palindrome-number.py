class Solution: 
    def isPalindrome(self, x): 

        '''
        1. a negative number will never be a palindrome
        2. a number which ends with 0 will never be a palindrome, till it is 0
        '''
        if x < 0 or (x % 10 == 0 and x != 0): 
            return False

        # storage
        reversed_half = 0


        while x > reversed_half: 
            # while the initial number if bigger then the reversed
            reversed_half = reversed_half * 10 + x % 10
            # x % 10 = will give us the modulo meaning the last digit of x
            x //= 10
            # remove the last digit from x

        return x == reversed_half or x == reversed_half//10
        '''
        - the 1st one is for even numbers 
        - and the 2nd one is for odd numbers
        = if the number had odd elements in the 1st place then the actual number and the reversed number will not have the same number of elements to then we would have to remove from the bigger number to make sure they match
        in this case the reversed half will always be the bigger one
        '''
