class Solution:
    def merge(self, nums1, m, nums2, n): 
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1 # thsi is done to get the actual index value of the lists that we have
        
        while p1 >= 0 and p2 >= 0: 
            if nums1[p1] > nums2[p2]: 
                nums1[p] = nums1[p1]
                p1 -= 1
            else: # nums1[p1] < nums2[p2]
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0: # this is so there are no left over values in the p2 or nume nums2 because if there are more elements in the p2 than the p2 then the p1 is going to end fast thats why this is done 
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
    
        # and we do not have to do the same for the p1 because we are storing all the values in the already existing p1 and tahst wwhy if teh p2 ends before p1 then we would just let them stay there

        return nums1 # coz we are storing all the values in nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

solution = Solution()
print(solution.merge(nums1, m, nums2, n))