class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        result = []

        for nums2 in arr2: 
            # yes it can handle if there are duplicates numbers before the subset of array2 appears in array1
            for i, nums1 in enumerate(arr1): 
                if nums1 == nums2: 
                    result.append(nums1)
                    arr1[i] = -1

        arr1.sort()
        for i in range(len(result), len(arr1)): 
            result.append(arr1[i])

        return result