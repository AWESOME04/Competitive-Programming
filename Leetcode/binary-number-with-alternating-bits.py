class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # bits = format(n, 'b')
        # n = len(bits)
        # l = 0
        # r = 1
        # inverting = True

        # if n == 1:
        #     return True
        # else:
        #     while r < n:
        #         if bits[l] != bits[r]:
        #             l += 1
        #             r += 1
        #         else:
        #             inverting = False
        #             break
        # return inverting

        # Bit Manipulation
        while n > 0:
            if ((n&1) ^ ((n>>1) & 1)) != 1:
                return False
            n >>= 1
        return True
