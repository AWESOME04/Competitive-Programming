class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def is_valid_state(state):
            if len(state) == k:
                return True
            return False

        def get_candidates(state):
            maxx = 1
            if state:
                maxx = max(state)
            arr = []
            for i in range(maxx, n+1):
                if i not in state:
                    arr.append(i)
            return arr

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
                return

            for candidate in get_candidates(state):
                state.add(candidate)
                search(state, solutions)
                state.remove(candidate)

        solutions = []
        state = set()
        search(state, solutions)
        return solutions

        # Time complexity: number of branches ** depth = O(n**k)
        # Space Complexity: Maximum depth = O(1)
        
        # Only the branching depends on the get candidates
