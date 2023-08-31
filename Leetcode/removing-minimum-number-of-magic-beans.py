class Solution:
  def minimumRemoval(self, beans: List[int]) -> int:
    n = len(beans)
    total = sum(beans)

    return min(total - (n - i) * bean
               for i, bean in enumerate(sorted(beans)))
