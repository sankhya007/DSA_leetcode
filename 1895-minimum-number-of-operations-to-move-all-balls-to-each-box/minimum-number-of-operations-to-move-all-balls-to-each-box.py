class Solution:
    def minOperations(self, boxes: str) -> list[int]:

        array = []
        result = []
        
        for i, box in enumerate(boxes):
            if box == '1': 
                array.append(i)
                # telling in which positions there is a 1 in the given string

        for i in range(len(boxes)): 
            # from each box index, negate the position index of the balls
            result.append(sum(abs(i - pos) for pos in array))

        return result