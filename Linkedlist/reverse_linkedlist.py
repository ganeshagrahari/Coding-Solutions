# Node class for linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

# Solution class with reverse method
class Solution:
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev    
# Create linked list: 3 -> 4 -> 5 -> 6 -> None
head = ListNode(3)
a = ListNode(4)
b = ListNode(5)
c = ListNode(6)

head.next = a
a.next = b
b.next = c

# Function to print linked list
def print_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    return " -> ".join(result) + " -> None"

# Test the linked list
print("Original list:")
print(print_list(head))

# Create solution instance and reverse the list
sol = Solution()
reversed_head = sol.reverse(head)

print("\nReversed list:")
print(print_list(reversed_head))