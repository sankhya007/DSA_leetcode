class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        
        length = len(flowerbed)

        for i in range(length): 
            if flowerbed[i] == 0:
                # either the pointer have to be at left or  if left position is 0 
                left_clear = (i == 0) or flowerbed[i - 1] == 0 
                # either the pointer have to be at the right or right position is 0
                right_clear = (i == length - 1) or flowerbed[i + 1] == 0 

                # if both clear
                if left_clear and right_clear:

                    flowerbed[i] = 1
                    n -= 1
                    if n <= 0: 
                        return True

        return n <= 0
