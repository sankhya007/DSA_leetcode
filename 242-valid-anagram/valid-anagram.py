class Solution():
    def isAnagram(self, s1, s2):
        return sorted(s1) == sorted(s2)