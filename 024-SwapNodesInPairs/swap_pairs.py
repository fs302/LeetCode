import json
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        lead = ListNode(0)
        lead.next = head
        p = lead
	# p is the former node, q is first node, r is second node. we should swap q-r.
        q = p.next
        while q is not None:
	    r = q.next
            if r is not None:
                q.next = r.next # q -> r.next
                p.next = r	# swap r to p.next
                r.next = q      # change r.next to q
                p = q           # p = p.next.next = q, that is skip 2 nodes
                q = p.next
            else:
                break

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
            head = stringToListNode(line)
            
            ret = Solution().swapPairs(head)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
