"""
Question:
Reverse a given sentence using recursion.
"""
def convert(lst): # converting a sentence into a list
    return (lst[0].split()) 

def reverse(List, revList): # reversing the list 
    if List == []:
        firstItem = revList.pop(0)
        revList.insert(5,firstItem)
        return revList
    else:
        firstItem = List.pop(0)
        revList.insert(1,firstItem)
        return reverse(List, revList)
        
def main():
    myList = ["I am a good girl"] 
    li = (convert(myList)) # converting a sentence into a list

    emptyList = []
    print ' '.join(word for word in reverse(li, emptyList))  # we are converting the reversed list into a sentence (reversed sentence).

if __name__ == "__main__":
    main()
