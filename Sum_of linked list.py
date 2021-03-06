#Write a program to add two linked list:
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = None
    temp = None
    carry = 0
    while l1 is not None or l2 is not None:
        sum_value = carry
        if l1 is not None:
            sum_value += l1.val
            l1 = l1.next
        if l2 is not None:
            sum_value += l2.val
            l2 = l2.next
        node = ListNode(sum_value % 10)
        
        carry = sum_value // 10
    
        if temp is None:
            temp = head = node
        # for any other node
        else:
            temp.next = node
            temp = temp.next
    if carry > 0:
        temp.next = ListNode(carry)
    return head


head1 = ListNode(2)
head1.next = ListNode(4)
head1.next.next = ListNode(3)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)

result = addTwoNumbers(head1, head2)
while result is not None:
    print(str(result.val), end=" ")
    result = result.next


