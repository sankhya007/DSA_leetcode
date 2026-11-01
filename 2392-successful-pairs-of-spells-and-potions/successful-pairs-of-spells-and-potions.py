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
                
            res.append(m - left)

        return res