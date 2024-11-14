def collatz_basic(n: int):
    if n < 1:
        raise ValueError("Number is not valid")
        
    steps = 0
    current = n
    
    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
        steps += 1
        
    return steps
    
    
# Time Complexity: O(log n) on average, but technically unbounded/unproven
# Space Complexity: O(1)


# Optimal Approach
class CollatzConjecture:
    def __init__(self):
        self.cache = {1: 0}
        
    def calculate_steps(self, n):
        if n < 1:
            raise ValueError("Number is not valid")

        origin = n
        numbers_encountered = []
        
        # Forward Path Finding
        while origin != 1:
            if origin in self.cache:
                break
            
            numbers_encountered.append(origin)
            
            if origin % 2 == 0:
                origin = origin // 2
            else:
                origin = (origin * 3) + 1
            
        
        # Get number of steps for the first cached values
        backtracked_steps = self.cache[origin]
        
        # Backtracking and Cache Updates
        while numbers_encountered:
            value = numbers_encountered.pop()
            backtracked_steps += 1
            self.cache[value] = backtracked_steps
            
        return self.cache[n]
            
# TC: O(log n) average case. 
# The while loop that follows the Collatz sequence takes O(log n) steps on average

# SC: Persistent Space (Cache): O(n)

