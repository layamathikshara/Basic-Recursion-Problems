"""
Question:
Write a more generalized predicate function called x-ish? that,
given two words, returns true if all the letters of the first word
are contained in the second.
"""
def letters(list_big, list_small, length, counter, leng):
    if counter == leng:
        return "Yes!"

    elif list_small[length] in list_big:
        counter = counter + 1
        return (letters(list_big, list_small, (length - 1), counter, leng))

    else:
        return "No!"

def main():
    small = "real"
    big = "generalized"

    list_small = list(small)
    list_big = list(big)

    length = (len(small)) - 1
    counter = 0
    leng = (len(small)) 

    print (letters(list_big, list_small, length, counter, leng))

if __name__ == "__main__":
    main()



