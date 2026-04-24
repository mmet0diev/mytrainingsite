from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1reversed = reversed(l1)
        l2reversed = reversed(l2)

        strsum1 = ""
        strsum2 = ""
        for n1 in l1reversed:
            strsum1 += str(n1)
        for n2 in l2reversed:
            strsum2 += str(n2)

        # print(strsum1)
        # print(strsum2)

        intsum1 = int(strsum1)
        intsum2 = int(strsum2)

        intsumresult = intsum1+intsum2
        


example = Solution()
example.addTwoNumbers([2,4,3], [5,6,4])