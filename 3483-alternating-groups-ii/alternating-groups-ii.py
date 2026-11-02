class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        left = 0
        n = len(colors)
        groups = 0 

        #start from 1 because left is already 0
        for right in range(1, n + k - 1): 
            # by adding the + k - 1 to the n we are creating an illution of an circular array, we can not add the whole array to the array itself because that will take a longer time that is why we are using the window length itself and adding that to the right side of the given array
            # and the -1 is there because when the left is at the last eleemnt of the given array and needs only k - 1 amount of elements to fulfill the criteria of maling the window that is why we add that and then modulo the artificial numbers to make it go back at its original position

            # if the last and the current element is same then we make the left move to right position 
            if colors[right % n] == colors[(right - 1) % n]: 
                left = right

            # window size more = left + 1
            if right - left + 1 > k: 
                left += 1
            
            # window size perfect and also passes the top constraint meaning the colours are alternating, count + 1
            if right - left + 1 == k: 
                groups += 1
            # if the size of the window is small nothing happens we just move over the right pointer to the next stage

        return groups