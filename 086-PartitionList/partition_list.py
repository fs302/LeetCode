import json
from typing import List 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # naive solution: convert to array
        preceder = []
        successor = []
        p = head 
        while p != None:
            if p.val < x:
                preceder.append(p.val)
            else:
                successor.append(p.val)
            p = p.next
        n_head = ListNode(0)
        p = n_head
        for v in preceder+successor:
            node = ListNode(v)
            p.next = node
            p = p.next
        return n_head.next

def main():
    head = ListNode(0)
    p = head
    arr = [1,3,4,2,2]
    for item in arr:
        node = ListNode(item)
        p.next = node
        p = p.next
    ret = Solution().partition(head.next, 2)
    p = ret
    while p != None:
        print(p.val)
        p = p.next 


if __name__ == '__main__':
    main()