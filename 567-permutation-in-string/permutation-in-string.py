class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # this just means this is not a sub-string
        if len(s1) > len(s2): 
            return False

        # give them a 26 length array, fully empty to store the counts
        countS1, countS2 = [0]*26, [0]*26
        # ord(s1[a]) - ord('a') = 0 
        # ord(s1[b]) - ord('a') = 1
        # this is how indexing works
        for i in range(len(s1)): 
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1

        # count how many matches we already have found, while moving in the length of s1
        matches = 0 # everything else will be zero to the matches will be close to 26 and not 0
        for i in range(26): 
            matches += (1 if countS1[i] == countS2[i] else 0)

        # because we have moved the length of s1, in both s1 and s2, we can start leaving out that partition itself
        left = 0 # left pointer
        for right in range(len(s1), len(s2)): # the left over space

            # if they already match all the characters return True
            if matches == 26: 
                return True 

            '''right'''
            # the letter right will be increased incrementally
            # in the current location, the letter's index
            index = ord(s2[right]) - ord('a')
            # because we have already seen that letter count + 1
            countS2[index] += 1

            # if they do match that means that number have appeared in both s1 and s2
            if countS1[index] == countS2[index]: 
                matches += 1
            # if we have to increase the count in s1 to match the count with s2 means the number did not match
            elif countS1[index] + 1 == countS2[index]: 
                matches -= 1


            '''left'''
            # the letter left will also be increased incrementally as the right element does
            index = ord(s2[left]) - ord('a')
            # again because the we are leaving out left
            countS2[index] -= 1

            # if the values does match then 
            if countS1[index] == countS2[index]: 
                matches += 1

            # the removal is happening because we leave the left out from the window meaning we are leaving that letter itself, which will not be in the further window 
            if countS1[index] - 1 == countS2[index]: 
                matches -= 1
            # left pointer increment
            left += 1

        # the match 
        return matches == 26


        

s1 = "ab"
s2 = "eidbaooo"

sol = Solution()
print(sol.checkInclusion(s1, s2))