class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Using bin + XOR
        # return bin((x ^ y)).count("1")

        xor = x ^ y
        res = 0

        while xor:
            res += xor & 1
            xor >>= 1
        return res
