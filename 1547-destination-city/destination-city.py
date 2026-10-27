class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        starts_with = {a for a, b in paths}
        # gather teh 1st element in starts with
        # final destination wil be present 1 time same as the start
        # compare the 2nd element with the elements in starts_with 
        # which ever is absent is the answer

        for a, b in paths: 
            if b not in starts_with: 
                return b