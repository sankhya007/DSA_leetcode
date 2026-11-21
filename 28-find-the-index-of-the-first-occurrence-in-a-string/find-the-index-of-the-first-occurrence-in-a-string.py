class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # if the needle does not exists then return 0, as instructed
        if len(needle) == 0: 
            return 0
        
        haystack_length = len(haystack)
        needle_length = len(needle)

        # if the needle length is bigger then invalid
        if needle_length > haystack_length: 
            return -1

        for start_index in range(haystack_length - needle_length + 1): 
            if haystack[start_index: start_index + needle_length] == needle: 
                return start_index
                # because we only have to return the 1st occurance
            
        return -1