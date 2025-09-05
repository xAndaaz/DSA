class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3: 
            return 0 
        l = [True] *n
        l[0]=l[1]= False
        for i in range(2,int(n**0.5)+1):
            if l[i] == True:
                l[i*i:n:i] = [False]*len(l[i*i:n:i])
        return sum(l)