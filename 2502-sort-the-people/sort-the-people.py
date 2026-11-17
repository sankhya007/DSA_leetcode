class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        result = []
        conbination = {}

        for name, height in zip(names, heights): 
            conbination[height] = name

        for h in reversed(sorted(heights)): 
            result.append(conbination[h])

        return result