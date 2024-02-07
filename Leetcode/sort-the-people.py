class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # n = len(heights)
        # Using Bubble sort

        # for i in range(n):
        #     for j in range(n-i-1):
        #         if heights[j] < heights[j + 1]:
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        #             names[j], names[j + 1] = names[j + 1], names[j]
        # return names

        # Using Selection sort
        # for i in range(n):
        #     min_idx = i

        #     for  j in range(i+1, n):
        #         if heights[min_idx] < heights[j]:
        #             min_idx = j
        #     heights[min_idx], heights[i] = heights[i], heights[min_idx]
        #     names[min_idx], names[i] = names[i], names[min_idx]
        # return names

        n = len(names)
        data = []

        for i in range(n):
            data.append((names[i], heights[i]))

        for i in range(n - 1):
            max_index = i
            for j in range(i + 1, n):
                if data[j][1] > data[max_index][1]:
                    max_index = j

            data[i], data[max_index] = data[max_index], data[i]

        sorted_names = [pair[0] for pair in data]

        return sorted_names
