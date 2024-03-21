class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates(head):
    curr = head
    while curr.next:
        temp = curr.next
        prev = temp
        while temp.next and temp.next.val == prev.val:
            prev = temp
            temp = temp.next
        curr.next = temp
        curr = curr.next
    while head:
        print(head.val)
        head = head.next
    return head

h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(3)
h.next.next.next.next = ListNode(4)
h.next.next.next.next.next = ListNode(4)
h.next.next.next.next.next.next = ListNode(5)

deleteDuplicates(h)
