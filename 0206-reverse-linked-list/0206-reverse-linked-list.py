class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        curr=head
        prev=None

        while curr:
            next_ptr=curr.next
            curr.next=prev
            prev=curr
            curr=next_ptr
        
        return prev

        # soln using an external stack
        # stack=[];
        # curr=head;
        # while curr:
        #     stack.append(curr.val);
        #     curr=curr.next;
        # curr=head;
        # while curr:
        #     curr.val=stack.pop();
        #     curr=curr.next;
        # return head;


