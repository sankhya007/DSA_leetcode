class Solution:
    def longestCommonPrefix(self, strings): 
        if not strings: 
            return "the strings list is empty."

        prefix = strings[0] 
        # asssign the 1st character of the list as the standerd to check the left overs in the list later on 
        for i in range(1, len(strings)): #leaving out the 1st and looping till the end 
            while not strings[i].startswith(prefix): # cheeck if the charcaters start with the assigned prefix
                prefix = prefix[:-1] # if not then -1 
                if not prefix: # means the prefix is empty(did not match with any of the exixting)
                    return ""

        return prefix

strings = strings = ["nigger", "nigga", "nga", "nigrow", "negro", "pablo"]
solution = Solution()
print(solution.longestCommonPrefix(strings))