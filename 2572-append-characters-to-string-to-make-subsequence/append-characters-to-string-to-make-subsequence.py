class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer = 0 
        for ch in s: 
            if pointer < len(t) and ch == t[pointer]: 
                pointer += 1

        return len(t) - pointer