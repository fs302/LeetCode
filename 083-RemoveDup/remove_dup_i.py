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
        p = head 
        while p is not None:
            while p.next is not None and p.val == p.next.val:
                q = p.next
                p.next = q.next
            p = p.next
        return head

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
    sorted_nums = [1,1,2,3,3,4,5,5,5]
    link_list = list_to_link(sorted_nums)
    res_link = s.deleteDuplicates(link_list)
    res = link_to_list(res_link)
    print(res)


if __name__ == '__main__':
    main()     