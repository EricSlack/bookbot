def sort_on(tup):
    return tup[1]

with open("books/frankenstein.txt") as f:
    letter={}
    ordered = []
    file_contents = f.read()
    wordcount = file_contents.split()
    file_contentsL = file_contents.lower()
    for char in file_contentsL:
        if char.isalpha():
            if char in letter:
                letter[char] += 1
            else:
                letter[char] = 1
    
    ordered = list(letter.items())
    ordered.sort(reverse= True, key = sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(wordcount)} words found in the document")
    print()

    for char in range(0,len(ordered)):
        print(f"The '{ordered[char][0]}' character was found {ordered[char][1]} times")
    
    print("--- End report ---")