# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Using the array approach
        # nums = []

        # while head:
        #     nums.append(head.val)
        #     head = head.next

        # # Using the two pointer technique
        # n = len(nums)
        # l, r = 0, n - 1

        # while l <= r:
        #     if nums[l] != nums[r]:
        #         return False
        #     l += 1
        #     r -= 1

        # return True

        # Optimized Solution - O(n) and O(1)

        # Find middle element
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse Linked List
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
