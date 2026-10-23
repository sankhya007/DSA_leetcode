# longest palindromic sub-string: leetcode 

class Solution(): 
    def longestPalindrome(self, s): 

        start = 0 
        end = 0 

        def expand(left, right): 

            # keep on moving forward if the letters keep matching
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                left -= 1 
                right += 1 

            # return back to the last check point if the one that we currently have is not matching
            return left+1, right-1

        for i in range(len(s)): 

            # odd and the even center is going to expand in the same rate and keep on going
            l1, r1 = expand(i, i)   # even 
            l2, r2 = expand(i, i+1) # odd

            '''
            two things this is going to make sure
            1. if the palindrome limiter getting bigger than the actual letter itself, if so then chop down
            2. if the string that we already have accounted for if that is actually smaller or equal than the one that we have currently have, if so - do nothing. 
            if bigger then replace the start and end
            '''
            if r1 - l1 > end - start: 
                start = l1
                end = r1 
            if r2 - l2 > end - start: 
                start = l2
                end = r2

        # end + 1 to include the last letter itself
        return s[start:end + 1]