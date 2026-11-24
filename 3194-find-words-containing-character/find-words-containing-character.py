class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        array = []
        for i, ch in enumerate(words): 
            if x in ch: 
                array.append(i)
        return array