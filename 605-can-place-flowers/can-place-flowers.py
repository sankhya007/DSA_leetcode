class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        if n == 0:
            return True

        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left_clear = (i == 0) or flowerbed[i - 1] == 0
                right_clear = (i == length - 1) or flowerbed[i + 1] == 0

                if left_clear and right_clear:
                    flowerbed[i] = 1
                    n -= 1
                    if n <= 0:
                        return True

        return n <= 0

        return n == 0
