class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merged = []
        i, j = 0, 0

        # till the increment is happenning in equal manner
        while i < len(word1) and j < len(word2): 
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        # after one side end and the other is left we have to keep going fo rthe left out side if the partition

        # if the word1 is bigger
        while i < len(word1): 
            merged.append(word1[i])
            i += 1

        # if the word2 is bigger
        while j < len(word2): 
            merged.append(word2[j])
            j += 1

        return "".join(merged)