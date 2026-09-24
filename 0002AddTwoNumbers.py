# Definition for singly-linked list.
# My Solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = 0
        dummy = ListNode(0)
        current = dummy
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10
            current.next = ListNode(digit)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

        

# Good Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        curr1 = l1
        curr2 = l2
        tail = dummy
        
        carry = 0

        while curr1 is not None or curr2 is not None:
            valor1 = curr1.val if curr1 is not None else 0
            valor2 = curr2.val if curr2 is not None else 0

            soma = valor1 + valor2 + carry

            digito = soma % 10
            carry = soma // 10
           
            if curr1:
                curr1 = curr1.next
            
            if curr2:
                curr2 = curr2.next

            novo_no = ListNode(digito)
            tail.next = novo_no
            tail = tail.next
        
        if carry != 0:
            no_carry = ListNode(carry)
            tail.next = no_carry
        
        return dummy.next