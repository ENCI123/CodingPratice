class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        s = list(s.split(' '))
        
        return len(s[len(s)-1])
