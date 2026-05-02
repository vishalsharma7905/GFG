'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        empty = Node(0)
        tail = empty
        
        while head1 and head2:
            if head1.data <=head2.data:
                tail.next = head1
                head1 = head1.next
                
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
            
        tail.next = head1 if head1 else head2
        return empty.next
            