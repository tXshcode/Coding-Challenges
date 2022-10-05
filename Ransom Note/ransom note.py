from asyncio.windows_events import NULL
from operator import truediv


class Solution(object):
    def canConstruct(self,ransomNote, magazine):
        x=0
        i=0
        for i in range(len(ransomNote)):
            if(not magazine):
                return False
            while(ransomNote[i] != magazine[x]):
                x=x+1
                if(x==len(magazine)):
                    return False
            magazine = magazine.replace(ransomNote[i],'',1)
            x = 0
        return True
        
        
    print(canConstruct("hi","abc","ab"))