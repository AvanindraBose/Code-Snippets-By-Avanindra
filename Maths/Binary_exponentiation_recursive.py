class Solution:
    def power(self , x : float, n : int) -> float :
        if n == 0 : 
            return 1
        res = 0
        half = self.power(x , n//2)
        if n%2 == 0 :
            # if divisible by 2
            res = half * half
        else :
            # if not then
            res = x * half * half
        
        return res

sol = Solution()
x = float(input("Please Enter the Number : "))
n = int(input("Please Enter the Power : "))
if n < 0 :
    x = 1/x
    n = -n

ans = sol.power(x,n)

print(f"The Number {x} raise to the power {n} is : {ans}")
