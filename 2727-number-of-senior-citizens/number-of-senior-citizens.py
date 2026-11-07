class Solution:
    def countSeniors(self, details): 
        # 11, 12 - age index 
        citizen = 0 

        for detail in details: 
            ch = detail[11] + detail[12]
            if int(ch) > 60: 
                citizen += 1

        return citizen