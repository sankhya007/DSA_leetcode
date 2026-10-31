class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        string = ""
        j = 0 
        l = len(spaces) - 1
        count = 0
        for ch in s: 
            if j <= l and count == spaces[j]: 
                string += " "
                j += 1
            string += ch
            count += 1

        return string
