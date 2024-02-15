class Solution:
    def findComplement(self, num: int) -> int:
        # Using bin

        # bit = bin(num)
        # n = len(bit)
        # res = []

        # for i in range(2, n):
        #     if bit[i] == "0":
        #         res.append(1)
        #     else:
        #         res.append(0)
        
        # ans = ''.join(map(str, res))
        # return int(ans, 2)
  
        # Using format

        # bit = list(format(num, 'b'))
        # n = len(bit)
        # res = []

        # for i in range(n):
        #     if bit[i] == "0":
        #         res.append(1)
        #     else:
        #         res.append(0)

        # ans = ''.join(map(str, res))
        # return int(ans, 2)

        # No use of inbuilt functions
        complement = ""

        while num > 0:
            if num % 2 == 1:
                complement += "0"
            else:
                complement += "1"
            num = num // 2

        return int(complement[::-1], 2)
