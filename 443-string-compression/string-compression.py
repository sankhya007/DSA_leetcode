class Solution:
    def compress(self, chars: list[str]) -> int:
        
        write = 0 
        i = 0

        while i < len(chars): 
            count = 0 
            ch = chars[i] # temp element for comparison
            while i < len(chars) and chars[i] == ch:
                i += 1 # increment or else this will be an infinite loop
                count += 1
            
            chars[write] = ch
            write += 1 

            if count > 1: 
                for d in str(count): 
                    chars[write] = d
                    write += 1

        return write