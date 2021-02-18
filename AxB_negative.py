"""
Question:
Write a function for mutliply(a, b) but you can only use the + or − operators.
"""

def Add(a, b, num):

    if (a or b) < 0:
        return "Pls enter a positive interger"

    elif a == 1:
        return b

    else:
        counter = b + num
        return Add(a - 1, counter, num)

def main():
    x = int(input("x Number:"))
    y = int(input("y Number:"))
    num = y 
    res = Add(abs(x), abs(y), abs(num))

    if((x>0 and y>0) or (x<0 and y<0)):
        print("Result", res)
        
    else:
        print("Result", -1 * res)

if __name__ == "__main__":
    main()