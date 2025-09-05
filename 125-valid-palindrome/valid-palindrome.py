class Solution:
    def isPalindrome( self, s: str) -> bool:
        s= s.lower()
        left = 0
        right = len(s)-1
        while left < right: 
            if s[left]== s[right] and s[left].isalnum() and s[right].isalnum() :
                left+=1
                right-=1
            elif s[left].isalnum() == False:
                left+=1    
            elif s[right].isalnum()== False :    
                right-=1
            else:
                return False
        return True      
            