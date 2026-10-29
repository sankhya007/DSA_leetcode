from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # n = len(nums)
        # res = 0 

        # for i in range(n): 
        #     current_sum = 0 
        #     for j in range(i, n): 
        #         current_sum += nums[j]
        #         if current_sum % k == 0: 
        #             res += 1 

        # return res 



        prefix_sum = 0 
        res = 0 
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        for n in nums: 
            prefix_sum += n 
            # take in one by one and see how much do we nee dto make the number divisible by 5
            remain = prefix_sum % k 

            # prefix_count[remain] += 1 
            # initially there is no remain and that is why we do have to add the remain and then from the next step count counting the remain 
            res += prefix_count[remain]
            prefix_count[remain] += 1 

        return res