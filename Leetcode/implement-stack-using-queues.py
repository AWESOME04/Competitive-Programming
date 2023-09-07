# class MyStack:
    # Implementation with List

    # def __init__(self):
    #     self.stack = []
    #     self.size = 0
        
    # def push(self, x: int) -> None:
    #     self.stack.append(x)
    #     self.size += 1

    # def pop(self) -> int:
    #     if self.size < 1:
    #         return None
    #     else:
    #         self.size -= 1
    #         return self.stack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def empty(self) -> bool:
    #     if self.size < 1:
    #         return True
    #     else:
    #         return False


# Implementation with Linked List
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyStack:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def push(self, x: int) -> None:
        new_node = ListNode(x)
        self.right.next = new_node
        new_node.prev = self.right
        self.right = new_node

    def pop(self) -> int:
        if self.right != self.left:
            popped = self.right
            self.right = self.right.prev
            return popped.val
        else:
            return None

    def top(self) -> int:
        if self.right != self.left:
            return self.right.val
        else:
            return None

    def empty(self) -> bool:
        return self.right.prev == self.left


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
