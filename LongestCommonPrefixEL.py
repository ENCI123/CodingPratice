class Solution:
    "Took longer time to finish"
    "Not Complete"
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==0):
            return ""
        
        reference = strs[0] 
        for i in range(1,len(strs)):
            CommonPrefix = ""
            if(len(reference) <= len(strs[i])):
                ind = len(reference)
            else:
                ind = len(strs[i])
            
            for j in range(ind):
                if reference[j] == strs[i][j]:
                    CommonPrefix = CommonPrefix + reference[j]
                   
                else:
                    break
                
            reference = CommonPrefix
            
           
        return reference
        
