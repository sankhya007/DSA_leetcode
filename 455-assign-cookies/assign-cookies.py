class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        i = j = 0 # i - students, j - cookie
        while i < len(g): 
            # if the student's greed is more than the given cookie, go up in cookie size
            while j < len(s) and g[i] > s[j]: 
                j += 1 
            # reached the end of cookie
            # dont care about students
            if j == len(s): 
                break
            i += 1
            j += 1

        return i 