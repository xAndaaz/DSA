#User function Template for python3

class Solution:
    def armstrongNumber (self, x):
        x = str(x)
        if int(x[0])**3+ int(x[1])**3+ int(x[2])**3 == int(x):
            return True 
        else :
            return False    
