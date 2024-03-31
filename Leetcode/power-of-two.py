class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # for x in range(0, 32):
        #     if pow(2, x) == n:
        #         return True
        # return False
        
        return n > 0 and n.bit_count() == 1
