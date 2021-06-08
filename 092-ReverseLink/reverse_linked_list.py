# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        leader = ListNode()
        leader.next = head
        # prepare-stage
        q = leader
        p = head 
        pos_num = 1
        while pos_num < left:
            q = q.next
            p = p.next
            pos_num += 1
        left_pointer = p 
        while pos_num < right:
            p = p.next 
            pos_num += 1
        right_pointer = p
        
        # operation-stage
        prev = q
        succ = right_pointer.next 
        
        p = left_pointer 
        q = p.next
        while p != right_pointer:
            r = q.next # save next-pointer
            q.next = p # reverse-link
            # step next
            p = q 
            q = r      
        # final joint
        prev.next = right_pointer 
        left_pointer.next = succ
        
        return leader.next

