class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd_ptr = head
        even_head = even_ptr = head.next

        while even_ptr and even_ptr.next:
            odd_ptr.next = odd_ptr.next.next
            odd_ptr = odd_ptr.next

            even_ptr.next = even_ptr.next.next
            even_ptr = even_ptr.next

        odd_ptr.next = even_head
        return head
