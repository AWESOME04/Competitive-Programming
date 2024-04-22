class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res = []
        title_list = title.split(" ")
        for word in title_list:
            if len(word) > 2:
                res.append(word.capitalize())
            else:
                res.append(word.lower())

        return " ".join(res)
