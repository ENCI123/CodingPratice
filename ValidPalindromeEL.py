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
        
        return result == result[::-1]  
        
