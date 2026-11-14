class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        starts_with = {a for a, b in paths}
        for a, b in paths: 
            if b not in starts_with: 
                return b