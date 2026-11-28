class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        count, max_count = 0, 0
        for sentence in sentences: 
            words = sentence.split(" ")
            count = len(words)
            max_count = max(count, max_count)
        return max_count