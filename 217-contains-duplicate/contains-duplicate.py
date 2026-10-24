class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        storage = set()
        for num in nums: 
            if num in storage: 
                return True
            storage.add(num)
        return False
                