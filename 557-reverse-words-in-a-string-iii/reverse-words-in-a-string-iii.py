class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(" ")

        for i, word in enumerate(words): 

            char = list(word)

            left = 0 
            right = len(char) - 1

            while left < right: 
                char[left], char[right] = char[right], char[left]
                left += 1
                right -= 1

            words[i] = "".join(char)

        return " ".join(words)
