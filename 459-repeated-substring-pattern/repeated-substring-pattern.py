class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        double_string = s + s
        first_index_after_zero = double_string.index(s, 1) # we start the find form 1
        return first_index_after_zero < len(s) # if the index gets found before the length itself ends that means the number is actually not repeated, and if it starts exacty after the length ends then it is where it should be and that is not repeated