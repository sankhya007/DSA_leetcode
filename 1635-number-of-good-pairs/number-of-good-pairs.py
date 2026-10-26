class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        # counter = 0

        # # bruite force, possible O(n^2) time complexity
        # for i in range(len(nums)): 
        #     for j in range(i+1, len(nums)): 
        #         if nums[i] == nums[j]: 
        #             counter += 1

        # return counter

        count = defaultdict(int)
        # kinds like enumerate but inside, while we do input
        res = 0 
        for num in nums: 
            # append to itself, everytime the value appears
            res += count[num]
            # append and give value
            count[num] += 1

        return res