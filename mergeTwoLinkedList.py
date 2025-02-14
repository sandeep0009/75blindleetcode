class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    

class Solution:
    def mergeTwoLinkedList(self,l1,l2):
        dummy=Node()
        current=dummy
        while l1 and l2:
            if l1.data<l2.data:
                current.next=l1
                l1=l1.next
            else:
                current.next=l2
                l2=l2.next
            current=current.next
        current.next=l1 or l2
        return dummy.next