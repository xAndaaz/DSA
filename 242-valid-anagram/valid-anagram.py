class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = {}
        ht= {}
        for index,item in enumerate (s):
            if item in hs:
                hs[item]+=1
            else:
                hs[item] =1     
        for index,item in enumerate (t):
            if item in ht:
                ht[item]+=1
            else:
                ht[item] =1        
        if ht==hs:
            return True
        return False    