class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[
        List[int]]) -> List[List[int]]:

        i = j = 0 
        array = []

        while i < len(nums1) and j < len(nums2): 
            if nums1[i][0] == nums2[j][0]:
                array.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1 

            elif nums1[i][0] < nums2[j][0]:
                array.append(nums1[i])
                i += 1

            else:
                array.append(nums2[j])
                j += 1

        array += nums1[i:] + nums2[j:]

        return array 