class Solution:
    def gcd(self, a, b):
        return a if b== 0 else self.gcd(b,a%b)
        
        