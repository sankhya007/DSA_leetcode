class Solution:
    def containsDuplicate(self, nums):
        storage = set()

        for num in nums:
            if num in storage:
                return True
            storage.add(num)

        return False