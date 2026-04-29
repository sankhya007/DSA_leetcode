class Solution:
    def groupAnagrams(self, strs): 
        anagram_storage = {} #creating a set for the indivisual anagram list
        for s in strs: 
            sorted_s = "".join(sorted(s)) # here we are sorting indivisual values in the list
            if sorted_s not in anagram_storage: 
                anagram_storage[sorted_s] = [] # create a empty list for that sorted value
            anagram_storage[sorted_s].append(s) # if it exists then append the value in that specific index
        return list(anagram_storage.values()) # calling the values as an output 

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
print(solution.groupAnagrams(strs))