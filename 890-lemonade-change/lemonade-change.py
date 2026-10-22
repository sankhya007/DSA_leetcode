# lemonade change 

class Solution():
    def lemonadeChange(self, bills): 

        five = 0 
        ten = 0 # we do not have to give out 20 doller bills because that is the max that we are going to get

        for bill in bills: 
            if bill == 5: 
                five += 1 
            elif bill == 10:
                if five == 0:
                    return False
                else: 
                    five -= 1 
                    ten += 1 

            else: # 20 doller bills
                if ten > 0 and five > 0: 
                    ten -= 1 
                    five -= 1 
                elif five >= 3: 
                    five -= 3 
                else: 
                    return False

        return True 

