class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        array = []

        for num in nums1: 
            if num not in nums2:
                continue
            else: 
                if num not in array: 
                    array.append(num)

        return array