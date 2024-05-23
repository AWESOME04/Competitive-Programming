class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)

        while R and D:
            DTurn = D.popleft()
            RTurn = R.popleft()

            if RTurn < DTurn:
                R.append(RTurn + len(senate))
            else:
                D.append(DTurn + len(senate))

        return "Radiant" if R else "Dire"
