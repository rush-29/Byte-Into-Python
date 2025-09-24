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


find_longest_word("This is a sentence with many different words!")
