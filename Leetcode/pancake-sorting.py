class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        end = len(arr)
        res = []

        while end > 1:
            max_ind = arr.index(end)
            if max_ind == end - 1:
                end -= 1
                continue

            if max_ind != 0:
                arr[:max_ind + 1] = reversed(arr[:max_ind + 1])
                res.append(max_ind + 1)

            arr[:end] = reversed(arr[:end])
            res.append(end)

            end -= 1
        return res
