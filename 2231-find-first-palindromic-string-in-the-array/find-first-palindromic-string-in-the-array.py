class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for num in words: 
            left = 0
            right = len(num) - 1
            while left <= right: 
                if num[left] != num[right]: 
                    break
                # if match, check for palindrome
                left += 1
                right -= 1
            else: 
                return num
        return ""