import math
from collections import defaultdict
class Solution:
    def sieve(self,n):
        prime = [1 for _ in range(n)]
        prime[0] = 0
        prime[1] = 0
        for i in range(2,int(math.sqrt(n))):
            if prime[i] == 1 :
                for j in range(i*i , n, i):
                    prime[j] = 0
        
        return prime
