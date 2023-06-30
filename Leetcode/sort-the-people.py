class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
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
