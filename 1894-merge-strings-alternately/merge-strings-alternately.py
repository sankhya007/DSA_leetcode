class Solution:
    def mergeAlternately(self, s1, s2): 
        merged = []
        i ,j = 0, 0
        while i < len(s1) and j < len(s2): 
            merged.append(s1[i])
            merged.append(s2[j])
            i += 1
            j += 1
        
        while i < len(s1): 
            merged.append(s1[i])
            i += 1
        while j < len(s2): 
            merged.append(s2[j])
            j += 1
        
        return "".join(merged)

s1 = "sankhya"
s2 = "bristi"

solution = Solution()
print(solution.mergeAlternately(s1, s2))