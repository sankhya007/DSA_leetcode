class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = int(a, 2)
        decimal_b = int(b, 2)
        decimal_sum = decimal_a + decimal_b
        binary_sum = bin(decimal_sum)[2:]
        # because it returns values like 0b101, the 1st two characters are unnecessary
        return binary_sum