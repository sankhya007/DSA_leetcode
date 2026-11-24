class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        array = [0] * len(indices)
        for ch, id in zip(s, indices):
            array[id] = ch 
        return "".join(array)