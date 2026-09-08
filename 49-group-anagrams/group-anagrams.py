class Solution(): 
    def groupAnagrams(self, strs): 
        
        # storage for anagrams 
        anagram_storage = {}

        # loop through the given array
        for s in strs: 
            
            # sort the indivisual words(done so that it is easy to find the anagrams)
            sorted_s = "".join(sorted(s))
            
            # check if anagram not in storage
            if sorted_s not in anagram_storage: 
                # if not then make a storage for anagram
                anagram_storage[sorted_s] = []

            # append the value in the new created storage
            anagram_storage[sorted_s].append(s)
        
        #return the lists alltogether
        return list(anagram_storage.values())