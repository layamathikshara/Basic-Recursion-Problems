"""
Question:
Reverse a given list using recursion.
"""
def reverse(List, revList):
    if List == []:
        firstItem = revList.pop(0)
        revList.insert(5,firstItem)
        return revList
    else:
        firstItem = List.pop(0)
        revList.insert(1,firstItem)
        return reverse(List, revList)
        
def main():

    myList = ["apple", "banana", "cherry", "orange", "grapes"]
    emptyList = []
    print reverse(myList, emptyList)

if __name__ == "__main__":
    main()
