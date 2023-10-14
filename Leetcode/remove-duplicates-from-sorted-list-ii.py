# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head
        dummy.next = cur

        # cur = head
        prev = dummy

        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur.next = cur.next.next
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next
