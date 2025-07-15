class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head):
        res = 0
        while head:
            res = res * 2 + head.val
            head = head.next
        return res
res=Solution().getDecimalValue(ListNode(1, ListNode(0, ListNode(1))))
print(res)