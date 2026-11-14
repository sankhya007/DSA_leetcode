class Solution:
    def check(self, nums: list[int]) -> bool:
        sortedNums = sorted(nums)
        array = []

        for i in range(len(nums)): 
            array.insert(0, sortedNums.pop())
            if nums == array + sortedNums: 
                return True

        return False