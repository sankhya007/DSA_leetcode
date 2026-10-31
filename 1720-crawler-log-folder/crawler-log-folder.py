class Solution:
    def minOperations(self, logs: list[str]) -> int:
        # depth = 0
        # for log in logs: 
        #     if log == "../": 
        #         if depth: 
        #             depth -= 1
        #     elif log != "./": 
        #         depth += 1
        # return depth

        stack = []
        for log in logs: 
            if log == "../": 
                if stack: 
                    stack.pop()
            elif log != "./": 
                stack.append(log)

        return len(stack)