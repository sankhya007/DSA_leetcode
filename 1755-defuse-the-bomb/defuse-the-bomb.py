class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        res = [0] * n 

        left = 0 
        current_sum = 0 
        
        for right in range(n + abs(k)): 
            current_sum += code[right % n]

            if right - left + 1 > abs(k): 
                current_sum -= code[left % n]
                left = (left + 1) % n 

            if right - left + 1 == abs(k):

                if k > 0: 
                    res[(left - 1) % n] = current_sum

                elif k < 0: 
                    res[(right + 1) % n] = current_sum

        return res
