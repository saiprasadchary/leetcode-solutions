class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow=head;
        fast=head;

        while fast and fast.next:
            
            slow=slow.next;
            fast=fast.next.next;
            if slow == fast:
                return True;
                
        return False;