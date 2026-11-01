class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
         
        # array = []

        # for i in range(len(spells)): 
        #     pairs = 0
        #     for j in range(len(potions)): 
        #         if spells[i] * potions[j] >= success: 
        #             pairs += 1  
        #     array.append(pairs)

        # return array


        potions.sort()
        m = len(potions)
        res = []

        for spell in spells: 
            left = 0 
            right = m - 1

            while left <= right: 
                mid = left + (right - left) // 2

                if spell * potions[mid] >= success:
                    right = mid - 1

                else: 
                    left = mid + 1
            # because the array is sorted anything before left is too weak, but left itself and anything after left will work 
            # m is the right of the array, and left is the 1st working one
            # if nothing works then left would be same as "m" itself, making the command append a zero
            res.append(m - left)

        return res