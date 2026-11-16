from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        count = Counter(words[0])

        for word in words: 
            current_count = Counter(word)
            for ch in count: 
                count[ch] = min(count[ch], current_count[ch])

        res = []
        for ch in count: 
            for i in range(count[ch]): 
                res.append(ch)

        return res