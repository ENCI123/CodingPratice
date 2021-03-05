class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sub_string =[]
        n = len(s)
        for i in range(n):
            temp=""
            for j in range(i,n):
                temp+=s[j]
                sub_string.append(temp)
                
        possible_result=[]
        for i in sub_string:
            if i==i[::-1]:
                possible_result.append(i)
                
        return max(possible_result,key = len)
