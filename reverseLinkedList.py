class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next



class Solution:
    def reverseLinkedList(self,head):
        prev=None
        current=head
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
        return prev
    
    def printList(self,head):
        while head:
            print(head.data,end=" ")
            head=head.next
        print()


head=Node(1)    
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)

sol=Solution()
sol.printList(head)
head=sol.reverseLinkedList(head)
sol.printList(head)
