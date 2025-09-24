# SOLUTIONS
# enter your solutions into this file

def find_longest_word(sentence):
    split_sentence = sentence.split(" ")

    longest_nchars = 0
    longest_word = ""

    for i in split_sentence:
        if len(i) > longest_nchars:
            longest_word = str(i)
            longest_nchars = len(i)

    print(f"Longest Word: {longest_word} | Length: {longest_nchars}")

def move_capitals_to_front(word):
    letters = []
    
    for i in word:
        if str(i).isupper():
            letters.insert(0, i)

        else:
            letters.append(i)

    print(letters)

move_capitals_to_front("eHllo")
