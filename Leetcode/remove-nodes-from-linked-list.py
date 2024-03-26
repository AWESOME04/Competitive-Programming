# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return

        # mono = []
        # curr = head
        # while curr:
        #     mono.append(curr.val)
        #     curr = curr.next

        # stack = []
        # for node in mono:
        #     while stack and stack[-1] < node:
        #         stack.pop()
        #     stack.append(node)

        # if len(stack) == 1:
        #     return ListNode(stack[0])

        # first, second = ListNode(stack[0]), ListNode(stack[1])
        # head = first
        # first.next = second
        # for i in range(2, len(stack)):
        #     curr = ListNode(stack[i])
        #     second.next = curr
        #     second = curr
        # return head

        # Using Recursion

        if not head:
            return None
        
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next
        return head
