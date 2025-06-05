# Add Two Numbers
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/add-two-numbers
# Description:
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each node contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify list construction
        dummy = ListNode(0)
        # Pointer to build the result list
        current = dummy
        # Carry to handle sums >= 10
        carry = 0

        # Continue while there are digits in either list or a carry
        while l1 or l2 or carry:
            # Get values from lists, use 0 if list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10  # Integer division for carry
            digit = total % 10   # Remainder for current digit

            # Create new node with the computed digit
            current.next = ListNode(digit)
            # Move to the next position
            current = current.next

            # Move to next nodes if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the result list, skipping the dummy node
        return dummy.next

# Test cases for local verification
if __name__ == "__main__":
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def print_linked_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    # Test case 1: 342 + 465 = 807
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print("Test 1:", print_linked_list(result))  # Expected: [7, 0, 8]

    # Test case 2: 0 + 0 = 0
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print("Test 2:", print_linked_list(result))  # Expected: [0]

    # Test case 3: 9999 + 1 = 10000
    l1 = create_linked_list([9, 9, 9, 9])
    l2 = create_linked_list([1])
    result = solution.addTwoNumbers(l1, l2)
    print("Test 3:", print_linked_list(result))  # Expected: [0, 0, 0, 0, 1]