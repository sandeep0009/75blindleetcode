class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next  



class Solution:
    def hasCycle(self,head):
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True
        return False