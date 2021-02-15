def shortestToChar(s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is
        the distance from index i to the closest occurrence of character c in s.
        The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
        """
        left,right,result = [None]*len(s),[None]*len(s),[None]*len(s)
        
        temp = float('inf')
        for i in range(len(s)):
            if s[i]==c:
                temp = 0
            left[i]=temp
            temp+=1

        temp = float('inf')
        for i in range(len(s)-1,-1,-1):
            if s[i]==c:
                temp = 0
            
            right[i]=temp
            temp+=1

        for i in range(len(s)):
            result[i]=min(left[i],right[i])
        return result
    
shortestToChar("loveleetcode","e")
