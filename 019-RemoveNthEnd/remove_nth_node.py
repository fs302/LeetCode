import json
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEndNaive(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        Time complexity: O(L) using list structure
        """
        if head.next == None:
            return None
        stack = []
        stack.append(head.val)
        while head.next != None:
            head = head.next
            stack.append(head.val)
        t = stack[:-n]
        if n == 1:
            t = stack[:-1]
        else:
            t.extend(stack[-n+1:])
        q = ListNode(t[0])
        newHead = q
        for v in t[1:]:
            p = ListNode(v)
            q.next = p
            q = p
        return newHead
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        Time complexity: O(L) only one pass 
        """
        lead = ListNode(0)
        lead.next = head
        first = lead
        second = lead
        for i in range(n):
            first = first.next
        while first.next != None:
            first = first.next
            second = second.next
        second.next = second.next.next
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

def stringToInt(input):
    return int(input)

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
            line = lines.next()
            n = stringToInt(line)
            
            ret = Solution().removeNthFromEnd(head, n)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()