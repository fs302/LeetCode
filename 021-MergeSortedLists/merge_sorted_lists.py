import json
import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lead = ListNode(0)
        keeper = lead
        p = l1
        q = l2
        while p is not None and q is not None:
            if p.val < q.val:
                keeper.next = p
                p = p.next
            else:
                keeper.next = q
                q = q.next
            keeper = keeper.next
        while p is not None:
            keeper.next = p
            p = p.next
            keeper = keeper.next
        while q is not None:
            keeper.next = q
            q = q.next
            keeper = keeper.next
        return lead.next

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            l1 = stringToListNode(line)
            line = lines.next()
            l2 = stringToListNode(line)
            
            ret = Solution().mergeTwoLists(l1, l2)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()