from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        head = ListNode()
        move = head
        pass_in = 0
        while p1 or p2 or pass_in != 0:
            sum = 0
            if p1 and p2:
                sum = p1.val + p2.val + pass_in
            elif p1:
                sum = p1.val + pass_in
            elif p2:
                sum = p2.val + pass_in
            else:
                sum = pass_in
            pass_in = sum // 10
            sum = sum % 10
            move.next = ListNode(sum)
            move = move.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        return head.next


