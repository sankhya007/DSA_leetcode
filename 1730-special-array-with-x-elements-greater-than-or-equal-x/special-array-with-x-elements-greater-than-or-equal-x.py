class Solution:
    def specialArray(self, nums: list[int]) -> int:

        for i in range(1, len(nums)+1): 
            count = 0 
            for num in nums: 
                if num >= i: 
                    count += 1

            if count == i: 
                return i 

        return -1

'''
okay so this is what we have to do to solev this problem
1st we have to go through the len of the given array 
then for per integer in len what we have to try to find if
if the nums that we have in that array are greater than that 
specific index or no, if no then we move to the next integer
and try to figure out the same thing again. When that number
matches we are going to return howmany numbr matched (greater
or more) because we are also figuring out the x itself that
is why x is mentioned as the magic number
'''