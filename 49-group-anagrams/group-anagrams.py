class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        anagram_storage = {}
        for ch in strs: 
            sorted_s = "".join(sorted(ch))
            if sorted_s not in anagram_storage: 
                anagram_storage[sorted_s] = []

            anagram_storage[sorted_s].append(ch)

        return list(anagram_storage.values())