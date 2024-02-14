class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None


class LinkedList:
    def __init__(self):
        self.head: Node = None

    def createLinkedListArr(self, arr: list):
        temp: Node = self.head
        for ele in arr:
            node = Node(ele)
            if temp is None:
                temp = node
                self.head = node
            else:
                temp.next = node
                temp = temp.next
        return self.head

    def traverse(self):
        if self.head is None:
            return
        else:
            temp: Node = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next
        return

    def rearrange_list(self):
        slow: Node = self.head
        fast: Node = self.head
        while fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        fast = self.head
        slow_head = slow.next
        slow.next = None

        while slow_head is not None:
            temp1 = fast.next
            temp2 = slow_head.next

            fast.head = slow_head
            slow_head.next = temp1

            fast = temp1
            slow_head = temp2

    def delete_duplicate(self):
        p = self.head

    def reverse_ll(self):
        prev = None
        p: Node = self.head

        while p:
            temp = p.next
            p.next = prev
            prev = p
            p = temp

        self.head = prev

    @staticmethod
    def sum_two_list(head1: Node, head2: Node):
        carry: int = 0
        res_head: Node = None
        temp: Node = None
        while head1 or head2:
            data1 = 0 if head1 is None else head1.data
            data2 = 0 if head2 is None else head2.data

            temp_data = data1 + data2 + carry
            carry = int(temp_data / 10)
            new_node = Node(int(temp_data % 10))
            if res_head is None:
                res_head = new_node
                temp = new_node
            else:
                temp.next = new_node
                temp = temp.next
            head1 = None if head1 is None else head1.next
            head2 = None if head2 is None else head2.next

        if carry != 0:
            temp.next = Node(carry)

        return res_head

    @staticmethod
    def slow_fast(head: Node):

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.data)
        if fast:
            print(fast.data)

    @staticmethod
    def intersect_two_ll(head1, head2):
        prev1 = None
        prev2 = None
        while head1:
            temp = head1.next
            head1.next = prev1
            prev1 = head1
            head1 = temp
        while head2:
            temp = head2.next
            head2.next = prev2
            prev2 = head2
            head2 = temp

        i: Node = None
        res = -1

        print("Intersect node:")
        while prev1 and prev2:
            if prev1.data != prev2.data:
                res = -1 if not i else i.data
                break
            i = prev1
            prev1 = prev1.next
            prev2 = prev2.next
        return res


ll = LinkedList()
a = ll.createLinkedListArr([3, 6, 9, 15, 30])
ll2 = LinkedList()
b = ll2.createLinkedListArr([10, 15, 30])

print(LinkedList.intersect_two_ll(a, b))
