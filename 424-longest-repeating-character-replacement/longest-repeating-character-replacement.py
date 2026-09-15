# longest repeating sub-string

class Solution(): 
    def characterReplacement(self, s, k): 

        # frequency of array for A to Z
        freq = [0] * 26 

        left = 0 
        max_count = 0 # count the most frequent character =
        max_length = 0 # count the max length of valid window

        # iterating the string with the right pointer(only the right pointer moves)
        for right in range(len(s)): 

            # increment the frequency of current character
            freq[ord(s[right]) - ord('A')] += 1 

            # update max_count with the max frequency seen so far
            max_count = max(max_count, freq[ord(s[right]) - ord('A')])

            # if the current window need more than K replacements, move left: 
            while (right - left + 1) - max_count > k: 
                freq[ord(s[left]) - ord('A')] -= 1 
                left += 1 

            max_length = max(max_length, right - left + 1)

        return max_length