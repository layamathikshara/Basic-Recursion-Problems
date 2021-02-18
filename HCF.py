"""
Question:
Find Greatest Common Divisor (GCD) of 2 numbers using recursion.
"""
def factors(a, b, num):
    if (a or b) < 0: # Negative Intergers
        return "Pls enter a positive integer"

    elif (a % num) == 0 and (b % num) == 0:
        return num
        
    else:
        return (factors(a, b, num - 1))

def main():
    n1 = 24
    n2 = 12
    print (factors(n1, n2, n1))

if __name__ == "__main__":
    main()
