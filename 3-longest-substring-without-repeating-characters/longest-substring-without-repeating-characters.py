# longest sub-string without repeating characters

class Solution(): 
    def lengthOfLongestSubstring(self, s): 

        storage = set()
        left = 0 
        max_length = 0 

        for right in range(len(s)): 
            # s[right] will keep incrementing one by one till it is in the storage keep deleting left and adding tight right and increment the left by 1
            while s[right] in storage: 
                storage.remove(s[left])
                left += 1 

            storage.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length