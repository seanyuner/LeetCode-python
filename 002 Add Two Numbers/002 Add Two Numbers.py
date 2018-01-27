# 138ms 39.35%
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            c1 = l1.val if l1 else 0
            c2 = l2.val if l2 else 0
            n.next = ListNode((c1 + c2 + carry) % 10)
            carry = (c1 + c2 + carry) / 10
            n = n.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next


# 152ms 20.97%
class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """ 
        res = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            nodesum = 0
            if l1:
                nodesum += l1.val
                l1 = l1.next
            if l2:
                nodesum += l2.val
                l2 = l2.next
            if carry:
                nodesum += 1
            n.next = ListNode(nodesum % 10)
            carry = nodesum / 10
            n = n.next
        return res.next


# 121ms 70.74%
class Solution3(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        res = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            nodesum = 0
            if l1:
                nodesum += l1.val
                l1 = l1.next
            if l2:
                nodesum += l2.val
                l2 = l2.next
            if carry:
                nodesum += 1
            n.next = ListNode(nodesum % 10)
            carry = nodesum / 10
            n = n.next
            
        return res.next
