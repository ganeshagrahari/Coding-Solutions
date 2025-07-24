class Solution:
    def midle_node(self,head) :
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow    
        