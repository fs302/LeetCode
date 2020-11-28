# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head

        # p is pre, q is current
        p, q = dummy, dummy.next

        while p is not None and q is not None:
            dup = False 
            # detection and skip duplication
            while q.next is not None and q.val == q.next.val:
                dup = True 
                q.next = q.next.next 
            # detect duplication, del all this element
            if dup:
                p.next = q.next # p remains
            else:
                p = p.next      # p go next
            q = p.next

        return dummy.next



def list_to_link(numbers):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    return dummyRoot.next

def link_to_list(head):
    res = [] 
    while head is not None:
        res.append(head.val)
        head = head.next
    return res

def main():
    s = Solution()
    nums = [1,1,2,3,4,4,5]
    link = list_to_link(nums)
    res_link = s.deleteDuplicates(link)
    res = link_to_list(res_link)
    print(res)


if __name__ == '__main__':
    main()             