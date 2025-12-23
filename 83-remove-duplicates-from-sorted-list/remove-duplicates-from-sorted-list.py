# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head
        seen = set()
        current = head
        seen.add(current.val) # Add the head's value to the set
        while current.next:
            if current.next.val in seen:
                # If duplicate, skip the next node
                current.next = current.next.next
            else:
                # If unique, add to set and move to the next node
                seen.add(current.next.val)
                current = current.next
        # Optional: If you need a standard Python list of unique values
        # unique_values_list = list(seen) 
        return head
            