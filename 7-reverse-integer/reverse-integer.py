class Solution:
    def reverse(self, x: int) -> int:
        a= str(x)
        if a[0] == "-":
            a = int("-"+a[:0:-1]) 
            if a > ((2**31)-1) or a < (-2**31):
                return 0
            else:
                return a
        else:
            a= int(a[::-1])
            if a > ((2**31)-1) or a < (-2**31):
                return 0
            return a        