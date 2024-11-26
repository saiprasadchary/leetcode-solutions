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
            return None;
        
        currA=headA;
        currB=headB;

        n1=0;
        n2=0;
        while currA:
            n1=n1+1;
            currA=currA.next

        while currB:
            n2+=1;
            currB=currB.next;

        currA=headA;
        currB=headB;
        if n2>n1:
            d=n2-n1;
            while d:
                currB=currB.next;
                d-=1;
        else:
            d=n1-n2;
            while d:
                currA=currA.next;
                d-=1;
        while currA and currB:
            if currA==currB:
                return currA;
            currA=currA.next;
            currB=currB.next;
        return None


        # dict1={};
        # curr=headA;
        # while curr:
        #     dict1[curr]=1;
        #     curr=curr.next;

        # curr=headB
        # print(dict1)
        # while curr:
        #     if curr in dict1:
        #         print(curr), 1
        #         return curr;
        #     curr=curr.next;
        # return None;

        # if not headA or not headB:
        #     return None

        # pA, pB = headA, headB

        # while pA is not pB:
        #     pA = pA.next if pA else headB
        #     pB = pB.next if pB else headA

        # return pA  # This will be either the intersection node or None if no intersection