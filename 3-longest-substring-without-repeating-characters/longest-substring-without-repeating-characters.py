class Solution:
    def lengthOfLongestSubstring(self, s): 
        storage = set()
        left = 0
        max_length = 0

        for right in range(len(s)): 
            while s[right] in storage: 
                storage.remove(s[left])
                left += 1

            storage.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

string = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(string))
