import json
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # Naive Implementation
    def getMinNode(self, lists):
        index = 0
        min_v = lists[0].val
        for i in range(1,len(lists)):
            if lists[i] is not None and lists[i].val < min_v:
                index = i
                min_v = lists[i].val
        return index, min_v
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        while None in lists:
            lists.remove(None)
        lead = ListNode(0)
        lead.next = None
        keeper = lead
        while len(lists) > 0:
            index, v = self.getMinNode(lists)
            p = lists[index]
            keeper.next = p
            keeper = p
            lists[index] = lists[index].next
            if lists[index] is None:
                del lists[index]
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

def stringToListNodeArray(input):
    listNodeArrays = json.loads(input)
    nodes = []
    for listNodeArray in listNodeArrays:
        nodes.append(stringToListNode(json.dumps(listNodeArray)))
    return nodes

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
            lists = stringToListNodeArray(line)
            
            ret = Solution().mergeKLists(lists)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()