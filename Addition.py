"""
Question
Add all the numbers from 1 to to n using recursion.
Example: n = 5 , Ans = 1 + 2 + 3 + 4 + 5 = 15
"""
def addition(n, y) :
    if (n == 0) :
        return y
    else :
        return (addition(n - 1, n + y))

n = 5
y = 0
print (addition(n, y))