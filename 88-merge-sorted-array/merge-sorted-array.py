class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        
        p1 = m - 1
        p2 = n - 1 
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1 
            else: 
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # if nums1 runs out before p2 we need to make sure that we have p2 down in the p1, and because we are placing them in p1 itself we do not need to worry about p1 not ending so that is why we are inly using the p2 block
        while p2 >= 0:
            # no condition just input
            nums1[p] = nums2[p2] 
            p2 -= 1
            p -= 1

        return nums1