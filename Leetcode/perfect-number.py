class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
            
        fact_sum = 1
        for fa in range(2, int(num**0.5)+1):
            if num % fa == 0:
                fact_sum += fa + num // fa

        return fact_sum == num
