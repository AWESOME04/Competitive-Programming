class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        prime = [True] * n
        prime[0] = False
        prime[1] = False

        for i in range(2, int(sqrt(n))+1):
            if prime[i]:
                for j in range(i+i, n, i):
                    prime[j] = False

        return prime.count(True)
        
