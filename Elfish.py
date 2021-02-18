"""
Question:
A word is considered elfish if it contains the
letters: e, l, and f in it, in any order.
Write a predicate function called elfish? that, given a word,tells us if that word is 
elfish or not.
"""

def check(word, length, counter):

    if length == 0:
        if ("e" and "l" and "f") in counter:
            return ("it is an elfish word")
        else:
            return "it is not an elfish word"

    elif word[length] in 'eElLfF':
        counter.append(word[length])
        return check(word, (length - 1), counter) 

    else:
        return check(word, (length - 1), counter)

def main():

    word = ("unfriendly")
    length = (len(word)) - 1
    counter = []
    print (check(word, length, counter))
    
if __name__ == "__main__":
    main()