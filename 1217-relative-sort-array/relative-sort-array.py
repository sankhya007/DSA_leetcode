class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        result = [] # where we are going to store everything

        # because arr2 is the smaller array and all the elements in arr2 will be in arr 1
        for nums2 in arr2: 
            # this the where we need to enumerate because where ever we are taking the values we are going to replace that with -1 rather than just removing that element so that when we actually ad the left overs we can use the indexes we have
            for i, nums1 in enumerate(arr1):
                if nums1 == nums2: 
                    # this will work for however many times nums1 appear in arr1
                    result.append(nums1)
                    arr1[i] = -1

        arr1.sort() # wil the left overs
        for i in range(len(result), len(arr1)): 
            # arr1 is the max length it can go upto anf the result is what ever that we have finished adding in the result so whatever is left is what wee have to add, and previously the sort() function has already sorted them so we can add them as is
            result.append(arr1[i])

        return result