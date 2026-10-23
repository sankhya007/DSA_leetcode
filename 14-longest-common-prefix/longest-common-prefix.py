# longest common prefix 

class Solution(): 
    def longestCommonPrefix(self, strs): 

        if not strs: 
            return "empty list!"

        # lets assume that the 1st element is the whole prefix
        prefix = strs[0]

        for i in range(1, len(strs)):

            # check if it starts with that or not
            while not strs[i].startswith(prefix): 
                # keep on decreasing that by 1 each time 
                prefix = prefix[:-1]

                # if word ends then return ""
                if not prefix: 
                    return ""

        return prefix 
