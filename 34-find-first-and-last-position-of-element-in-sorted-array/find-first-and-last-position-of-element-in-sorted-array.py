# find first and last position of element in sorted array 

class Solution(object):
    def searchRange(self, nums, target):
        
        def findFirst(): 

            left = 0 
            right = len(nums) - 1

            # if not found return -1
            ans = -1 

            while left <= right: 

                mid = left + (right - left) // 2 

                # if target found, check if there is same number on the left of that 
                if nums[mid] == target: 
                    ans = mid 
                    right = mid - 1 

                elif nums[mid] < target: 
                    left = mid + 1 

                else: 
                    right = mid - 1 

            return ans


        def findLast(): 

            left = 0 
            right = len(nums) - 1

            ans = -1 

            while left <= right: 

                mid = left + (right - left) // 2 

                # if target found, check if there is same number on the right side of that 
                if nums[mid] == target: 
                    ans = mid
                    left = mid + 1 

                elif nums[mid] < target: 
                    left = mid + 1

                else: 
                    right = mid - 1 

            return ans

        return [findFirst(), findLast()]


sol = Solution()

nums = [5,7,7,8,8,10]
target = 8

print(sol.searchRange(nums, target))