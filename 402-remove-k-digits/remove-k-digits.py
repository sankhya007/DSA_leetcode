class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for ch in num: 
            while k and stack and stack[-1] > ch: 
                # append an element in the stack, if the element is smaller than the current element in num pop that and keep the current element in stack
                stack.pop()
                k -= 1
            stack.append(ch)

        # also, if the k did not reach 0, remove form the last 
        if k: 
            stack = stack[:-k]

        # strip any 0 that are on the left of the stack
        return "".join(stack).lstrip("0") or "0"