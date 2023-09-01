# Create class Node for Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Define the Linked List class
class MyLinkedList:
    def __init__(self):
        # Creating dummy nodes left and right
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node, prev, next = Node(val), self.left, self.left.next
        prev.next = new_node
        next.prev = new_node
        new_node.prev = prev
        new_node.next = next

    def addAtTail(self, val: int) -> None:
        new_node, prev, next = Node(val), self.right.prev, self.right
        prev.next = new_node
        next.prev = new_node
        new_node.prev = prev
        new_node.next = next

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            new_node, prev, next = Node(val), cur.prev, cur
            prev.next = new_node
            next.prev = new_node
            new_node.prev = prev
            new_node.next = next

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            prev, next = cur.prev, cur.next
            prev.next = next
            next.prev = prev
