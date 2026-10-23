# group anagrams

class Solution(): 
    def groupAnagrams(self, strs): 

        anagram_storage = {}

        for s in strs: 

            # "eat" → ['a', 'e', 't']
            # "aet" (after the joining is done)
            sorted_s = "".join(sorted(s))

            # "eat" - "aet"
            # "aet" - "aet"
            # "tea" - "aet"
            # so basically aet is the value if the storage in which the word is getting in

            # if the value does not already exist we create a new storage and then add that value to it
            if sorted_s not in anagram_storage: 
                anagram_storage[sorted_s] = []

            # append the value in the respective storage
            anagram_storage[sorted_s].append(s)

        # list the values as said
        return list(anagram_storage.values())