class Solution: 
    def isPalindrome(self, head): 
        slow = head
        fast = head
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
        prev = None
        current = slow
        while current: 
            next_val = current.next
            current.next = prev
            prev = current
            current = next_val
        left = head
        right = prev
        while right:
            if left.val != right.val: 
                return False
            left = left.next
            right = right.next
        return True