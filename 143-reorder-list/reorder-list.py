class Solution: 
    def reorderList(self, head): 
        if not head or not head.next: 
            return 
        slow = head 
        fast = head.next # next val 
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next 
        second = slow.next # placeholder
        prev = slow.next = None 
        while second: 
            temp = second.next 
            second.next = prev 
            prev = second
            second = temp
        first = head 
        second = prev
        while second: 
            temp1, temp2 = first.next, second.next 
            first.next = second 
            second.next = temp1
            first, second = temp1, temp2 # increment 
