class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        result = ""
        for strs in s:
            if strs.isalnum():
                result = result + strs.lower()
        
        comparison = ""
        i = len(result)-1
        while(i>=0):
            comparison = comparison + result[i]
            i = i-1
            
        if result == comparison:
            return True
        else:
            return False
