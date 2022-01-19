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
        # print(head, head.val, head.next)
        # head = head.next
        # print(head, head.val, head.next)
        if head==None:
            return None
        visited = []
        while(True):
            if (head.next==None):
                return None
            if head.next in visited:
                return head.next
            visited.append(head)
            head = head.next
        return None