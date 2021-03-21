from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0
        for bill in bills:
            if bill == 5:   # 不需要找零
                five += 1
            if bill == 10:  # 用5找零
                ten += 1
                if (five <= 0):
                    return False 
                five -= 1        
            if bill == 20:  # 用10， 5|5，5，5找零
                twenty += 1
                if (ten > 0 and five > 0):
                    ten -= 1
                    five -= 1
                elif (ten <= 0 and five >= 3):
                    five -= 3
                else:
                    return False
        return True