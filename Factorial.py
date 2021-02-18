"""
Question:
Find the factorial of a number using recursion.
"""

# step by step explanition
# number = 3
# fcatorial(3) = 3 * 2 * 1
# factorial(2) = 2 * 1
# factorial(1) = 1 * 0
# factorial(3) = 3 * factorial(2)

def factorial(number, fac):
    if number < 0:
        return ("pls enter a whole number.")

    elif number == 0:
        return fac # Exit condition

    elif number > 0:
        fac = number * fac
        return factorial(number - 1, fac) 

def main():
    
    number = input("Enter Number:")
    fac = 1
    print(factorial(number, fac))

if __name__ == "__main__":
    main()
