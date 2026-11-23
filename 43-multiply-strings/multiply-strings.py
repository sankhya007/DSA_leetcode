class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0": 
            return "0"

        len1, len2 = len(num1), len(num2)

        # answer can not exceed the length of the number combined, either it'll be the same or need less space
        result = [0] * (len1 + len2)

        for i in range(len1-1, -1, -1): 
            digit1 = int(num1[i])

            for j in range(len2-1, -1, -1): 
                digit2 = int(num2[j])

                result[i + j + 1] += digit1 * digit2

        for i in range(len1 + len2 - 1, 0, -1): 
            # // gives us the 1st digit(carry), % gives us the later digit
            result[i-1] += result[i] // 10 
            result[i] %= 10

        # because the numbers does not really have zero in them so the answer has to have same number of digit as combined given numbers or one less, that is what we are figuring out here
        start_index = 0 if result[0] != 0 else 1

        # so now we start form start index, and turn every digit into string and join them
        return "".join(str(digit) for digit in result[start_index:])
