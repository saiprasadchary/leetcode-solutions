# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummyNode=ListNode(-1);
        currNode=dummyNode;
        carry=0;
        while l1 or l2:
            sum1=carry;
            if l1:
                sum1+=l1.val;
                l1=l1.next;
            if l2:
                sum1+=l2.val;
                l2=l2.next;
            newNode=ListNode(sum1%10);
            carry=sum1//10;
            currNode.next=newNode;
            currNode=currNode.next;

            if carry:
                newNode=ListNode(carry);
                currNode.next=newNode

        return dummyNode.next


        
        


            
            


        