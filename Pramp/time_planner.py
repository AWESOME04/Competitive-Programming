"""
Time Planner

Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, 
returns the earliest time slot that works for both of them and is of duration dur. 
If there is no common time slot that satisfies the duration requirement, return an empty array.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. 
The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. 
The input variable dur is a positive integer that represents the duration of a meeting in seconds. 
The output is also a pair represented by an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed, i.e, 
time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.


input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: [] # since there is no common slot whose duration is 12

"""

def meeting_planner(slotsA, slotsB, dur):
  l, r = 0, 0
  m, n = len(slotsA), len(slotsB)
  
  while l < m and r < n:
    slotsA_start, slotsA_end = slotsA[l] 
    slotsB_start, slotsB_end = slotsB[r]
    
    start = max(slotsA_start, slotsB_start)
    end = min(slotsA_end, slotsB_end)
    
    result = end - start
    if result >= dur:
      return [start, start + dur]
    
    
    if slotsA_end < slotsB_end:
      l += 1
    else:
      r += 1
  
      
  return []  

# TC: O(m + n) time
# SC: O(1) space