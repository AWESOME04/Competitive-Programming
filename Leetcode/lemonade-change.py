class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        bill_five = 0
        bill_ten = 0

        for i in range(n):
            if bills[i] == 5:
                bill_five += 1
            elif bills[i] == 10:
                if bill_five == 0:
                    return False
                bill_ten += 1
                bill_five -= 1
            else:
                if (bill_five>=1 and bill_ten >= 1):
                    bill_five -= 1
                    bill_ten -= 1
                elif bill_five >= 3:
                        bill_five -= 3
                else:
                    return False
        return True
            
