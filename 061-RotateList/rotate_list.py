# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # get length of link
        n = 0
        p = head 
        while p is not None:
            n += 1
            p = p.next
        
        if n <= 1:
            return head
        
        # omit repeat
        k = k % n
        if k == 0:
            return head
        
        # find new head, which is at position n-k
        p = head 
        cnt = 0
        while cnt < n - k - 1:
            p = p.next 
            cnt += 1
        q = p.next 
        newHead = q

        # transform
        p.next = None 
        while q is not None and q.next is not None:
            q = q.next 
        q.next = head 
        return newHead

        
def travel(link):
    p = link
    while p is not None:
        print(p.val)
        p = p.next

def main():
    link = ListNode(0)
    head = link
    item_list = [1,2,3]
    for item in item_list:
        p = ListNode(item)
        link.next = p 
        link = p
    head = head.next
    travel(head)
    print()
    k = 3

    s = Solution()
    newLink = s.rotateRight(head, k)
    travel(newLink)
    
    

if __name__ == '__main__':
    main()