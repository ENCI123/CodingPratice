#One error, missing "aa" "a" scenario
class Solution:
        def longestCommonPrefix(self,strs: List[str]) -> str:
            if(len(strs) == 0):#check empty list
                return ""
            answer = strs[0]#start with the first value
            for s in range(len(strs)-1):#compare it to all other values
                if(answer == ""):#if first value is empty string return
                    break
                curWord = strs[s+1]
                if(len(curWord)<len(answer)):#scenario when curword is shorter but equal
                    setCurWord = 1
                    for c in range(len(curWord)):#cycle through letters until difference is found
                        if(answer[c] != curWord[c]):#split string at index of difference and break
                            answer = answer[0:c]
                            setCurWord = 0
                            break
                    if(setCurWord):#if curword is short, and no differences were found, update answer
                        answer = curWord
                else:
                    for c in range(len(answer)):#cycle through letters until difference is found
                        if(answer[c] != curWord[c]):#split string at index of difference and break
                            answer = answer[0:c]
                            break
            return answer
