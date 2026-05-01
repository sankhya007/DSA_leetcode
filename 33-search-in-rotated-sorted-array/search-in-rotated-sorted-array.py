class Solution:
    def search(self, nums, target): 
        left = 0 
        right = len(nums) - 1
        
        while left <= right: 
            mid = left + (right - left) // 2
            #again this iss the only way to get the mid

            if nums[mid] == target: 
                return mid 
            # if the target is mid, to get the final answer

            elif nums[left] <= nums[mid]: 
            # if the target is in the 1st half 
                if nums[left] <= target < nums[mid]: 
                    right = mid - 1
                else:
                # if the search fail for the 1st half
                    left = mid + 1

            else:
            # if the target is in the 2nd half 
                if nums[mid] < target <= nums[right]: 
                    left = mid + 1
                else: 
                # if the search faiil for the 2nd half meaning this is in the 1st half
                    right = mid -1
        
        return -1 
        # if you do not find the target return -1, as result not found

nums = [4,5,6,7,0,1,2]
target = 0

solution = Solution()
print(solution.search(nums, target))