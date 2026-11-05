class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0 
        res = 0 
        count = defaultdict(int)
        # because we need to have a hashmap counter if the array that we are goign through

        for right in range(len(s)): 
            count[s[right]] += 1 

            # only when the string have all the values a,b,c then we are going to apply that
            while len(count) == 3: 

                # because then we have teh number of ways in which we can write the given string
                res += (len(s) - right)

                # when we do reach this level then we have to slide the window and delete left
                count[s[left]] -= 1

                # and when the value of left actually hits zero that means we just do not have that character in the hashmap any more and that is why we have to go to the array and keep on addign to the count variable till we actually find the variable that we need to complete the a,b,c
                if count[s[left]] == 0: 
                    count.pop(s[left])
                left += 1 

        return res