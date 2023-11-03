class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def is_valid_state(state):
            # check if it is a valid solution
            return True

        def get_candidates(state):
            candidates = []
            for num in nums:
                if num not in state:
                    candidates.append(num)
            return candidates

        def search(state, start_id, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
                # return

            for i in range(start_id, len(nums)):
                candidate = nums[i]
                state.add(candidate)
                search(state, i + 1, solutions)
                state.remove(candidate)


        solutions = []
        state = set()
        search(state,0, solutions)
        return solutions
