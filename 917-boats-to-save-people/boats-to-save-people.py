class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:

        people.sort()
        boats = 0 

        left = 0 
        right = len(people) - 1

        while left <= right: 
            # if the lightest and te heaviest person fits then move them together 
            # both the left and the right gets incremented 
            if people[left] + people[right] <= limit: 
                left += 1

            # if only the heaviest person fits then add then and only increment right, we have to retry for the light person with the 2nd heaviest person
            right -= 1 

            boats += 1

        return boats