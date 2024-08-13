# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 23:06:48 2024

@author: hayde
"""

class Node:
    def __init__(self, element, next=None):
        self.element = element  # A reference to the value
        self.next = next        # A reference to the next node

def is_palindrome(node):
    if not node or not node.next:
        return True
    
    # Step 1: Use the two-pointer technique to find the middle of the list
    slow = node
    fast = node
    prev = None
    
    while fast and fast.next:
        fast = fast.next.next
        
        # Reverse the first half of the list
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node
    
    # If the number of elements is odd, skip the middle element
    if fast:
        slow = slow.next
    
    # Step 2: Compare the reversed first half with the second half
    first_half = prev
    second_half = slow
    
    while first_half and second_half:
        if first_half.element.lower() != second_half.element.lower():
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True