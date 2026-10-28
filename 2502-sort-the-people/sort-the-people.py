class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        height_to_name = {}
        for name, height in zip(names, heights): 
            height_to_name[height] = name

        result = []
        for h in reversed(sorted(heights)): 
            result.append(height_to_name[h])

        return result