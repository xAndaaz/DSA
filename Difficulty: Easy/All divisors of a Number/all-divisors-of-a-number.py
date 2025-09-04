#User function Template for python3
import math
class Solution:
    def print_divisors(self, x):
        tup = []
        lol = int(math.sqrt(x))
        for i in range(1, lol+1, 1):
            if x % i == 0:
                tup.append(i)
                if(i != x/i):
                    tup.append(int(x/i))
        tup.sort()
        print(" ".join(str(n) for n in tup), end=" ")