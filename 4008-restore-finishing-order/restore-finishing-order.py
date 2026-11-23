class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        for num in order: 
            if num not in friends: 
                continue 
            else:
                ans.append(num)
        return ans