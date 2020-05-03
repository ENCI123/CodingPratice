class Solution:
    "Took longer time to finish"
    "Not Complete"
    def longestCommonPrefix(self, strs: List[str]) -> str:
        CommonPrefix = ""
        reference = strs[0]
        result = ""
        for i in range(len(strs)-1):
            i = i+1
            if(len(reference) <= len(strs[i])):
                ind = len(reference)
            else:
                ind = len(strs[i])
            for j in range(ind):
                if reference[j] == strs[i][j]:
                    CommonPrefix =  CommonPrefix+reference[j]
                    
                
            reference = CommonPrefix
            
        return reference
        
