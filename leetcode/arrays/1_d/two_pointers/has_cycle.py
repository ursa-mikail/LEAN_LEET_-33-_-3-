class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    """
    Detect if a linked list has a cycle.
    Return True if cycle exists, False otherwise.
    
    Example: 3 → 2 → 0 → -4 → (back to 2) → True
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

# Test case creation
def create_linked_list_with_cycle(values, pos):
    """Create a linked list with cycle at position pos (-1 if no cycle)"""
    if not values or pos == None:
        return None
    
    head = ListNode(values[0])
    current = head
    nodes = [head]
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    
    if pos != -1 and pos < len(nodes):
        current.next = nodes[pos]
    
    return head

# Test cases
list1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)  # Cycle at node index 1
list2 = create_linked_list_with_cycle([1, 2], 0)         # Cycle at node index 0  
list3 = create_linked_list_with_cycle([1], None)           # No cycle

print(has_cycle(list1))  # True
print(has_cycle(list2))  # True  
print(has_cycle(list3))  # False

"""
True
True
False
"""