import json

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# def linkListToString(head):
#     p = head
#     st = str(head.val)
#     p = p.next
#     while p is not None:
#         st = st +  '->' + str(p.val) 
#         p = p.next
#     return st

class Solution(object):
    def reverse_link(self, group_prev, group_tail):
        group_head = group_prev.next
        succ = group_tail.next
        p = group_prev
        q = p.next              # CURRENT Pointer, init by group head
        while q is not None and q != succ:
            r = q.next
            q.next = p
            p = q
            q = r
        group_prev.next = group_tail
        group_head.next = succ
        group_tail = group_head
        return group_prev, group_tail
        
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        lead = ListNode(0)
        lead.next = head
        
        group_prev = lead
        group_head = group_prev.next
        
        pointer = group_head
        counter = 1
        
        while pointer is not None:
            if counter == k:
                # change head-tail
                group_prev, new_pointer = self.reverse_link(group_prev, pointer)
                # start next journey
                group_prev = new_pointer
                group_head = group_prev.next
                pointer = group_head
                counter = 1
            else:
                pointer = pointer.next
                counter += 1
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
            k = stringToInt(line)
            
            ret = Solution().reverseKGroup(head, k)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()