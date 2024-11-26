# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA  # This will be either the intersection node or None if no intersection