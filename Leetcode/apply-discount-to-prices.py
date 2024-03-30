class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        res = sentence.split(" ")
        for i in range(len(res)):
            if res[i][0] == "$" and len(res[i]) >= 2 and res[i][1:].isdigit():
                new_val = int(res[i][1:]) - (int(res[i][1:]) * (discount / 100))
                res[i] = "${:.2f}".format(new_val)

        ans = " ".join(res)
        return ans
