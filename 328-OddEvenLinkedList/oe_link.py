# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        origin = head
        extra_link, extra_link_tail = None, None
        while head != None and head.next != None:
            p = head.next
            # 修改奇数链
            head.next = p.next 
            p.next = None
            # 初始化偶数链
            if extra_link == None:
                extra_link = p
            # 导入偶数链队尾
            if extra_link_tail != None:
                extra_link_tail.next = p
                extra_link_tail = extra_link_tail.next
            else:
                extra_link_tail = p
            if head.next == None:
                break            
            head = head.next

        head.next = extra_link
        return origin