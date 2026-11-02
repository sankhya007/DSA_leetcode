from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count = defaultdict(int)
        left, total, res = 0, 0, 0

        for r in range(len(fruits)): 
            count[fruits[r]] += 1
            total += 1

            # length more than 2 means there are more than 2 types of fruits that we have picked
            while len(count) > 2: 
                f = fruits[left] # temporary element, delete one fruit from the count for this, because we are taking this one fruit as a reference fruit 
                count[f] -= 1 # decrease the count
                total -= 1 # total gets decreased
                left += 1 # left pointer goes up

                if not count[f]: # if the count in 0
                    count.pop(f)

            res = max(res, total)

        return res


fruits = [1,2,3,2,2]
sol = Solution()
print(sol.totalFruit(fruits))