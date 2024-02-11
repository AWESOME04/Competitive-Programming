class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n == 2:
            return skill[0] * skill[1]
        
        minn = min(skill)
        maxx = max(skill)
        
        skill.sort()
        l = 0
        r = n - 1
        chemistry = []
        tot = minn + maxx

        while l < r:
            if skill[l] + skill[r] == tot:
                chemistry.append(skill[l]*skill[r])
                l += 1
                r -= 1
            elif skill[l] + skill[r] < n:
                l += 1
            else:
                r -= 1
        
        if not chemistry or len(chemistry) != n // 2:
            return -1
        else:
            return sum(chemistry)


        #TC: O(nlog(n))
        # SC: O(n)
