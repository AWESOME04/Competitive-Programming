class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        match = 0
        
        for i in range(len(s2)):
            if s2[i] in s1_map:
                s1_map[s2[i]] -= 1
                if s1_map[s2[i]] == 0:
                    match += 1
                    
            if i + 1 > len(s1):
                left = s2[i - len(s1)]
                if left in s1_map:
                    s1_map[left] += 1
                    if s1_map[left] == 1:
                        match -= 1
            
            if match == len(s1_map):
                return True

        return False
