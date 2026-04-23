class Solution:
    def firstUniqChar(self, s): 
        char_set = {}   # creating an empty set 

        for char in s: 
            char_set[char] = char_set.get(char, 0) + 1
            # this line is going to save the characters like this : {l:1, e:2, t:1.......}

        for i,char in enumerate(s): # seeing which character has 1 in count and returning that 
        # we did enumate here to keep the output like a 1 , b 2 , c 3
            if char_set[char] == 1: 
                return i

        return -1

string = "leetcode"
solution = Solution()
print(solution.firstUniqChar(string))

        