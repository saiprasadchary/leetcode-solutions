# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None;
            
        slow=fast=head;

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next;
            if(fast==slow):
                break;
            
        else:
            return None;
        
        slow=head;
        
        while slow!=fast:
            slow=slow.next;
            fast=fast.next;
        return slow;
        






        # if head is None:
        #     return None;

        # visited=set();
        # curr=head;

        # while curr:
        #     if curr in visited:
        #         return curr;
        #     visited.add(curr)
        #     curr=curr.next;
            
        # return None;