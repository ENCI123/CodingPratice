# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1=""
        temp2=""
        while(l1!=None):
            temp1+= str(l1.val)
            l1 = l1.next
    
        while(l2!=None):
            temp2+=str(l2.val)
            l2 = l2.next
        temp1 =temp1[::-1]
        temp2 = temp2[::-1]
        result = str(int(temp1)+int(temp2))
        
        
        cur = dummy = ListNode(0,None)
        for i in result[::-1]:
            cur.next = ListNode(i,None)
            
            cur = cur.next
        return dummy.next
