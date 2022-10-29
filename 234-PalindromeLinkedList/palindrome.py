# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Naive: convert to list, scan from two sides
        # Time O(n)
        # Memory O(n), Can be optimize to One Number, But time consuming

        input_list = []
        while head != None:
            input_list.append(head.val)
            head = head.next 

        return input_list == input_list[::-1]