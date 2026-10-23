class Solution(): 
    def groupAnagrams(self, strs): 

        anagram_storage = {}

        for s in strs: 

            sorted_s = "".join(sorted(s))

            if sorted_s not in anagram_storage:
                anagram_storage[sorted_s] = []

            anagram_storage[sorted_s].append(s)

        return list(anagram_storage.values())