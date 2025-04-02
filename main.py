def get_index(word_leng):
    leng = len(word_leng)
    while True:
        index = input("Enter an index (-1 to quit): ")
        if int(index) == -1:
            return "no"
        elif int(index) < 0 :
            print("Invalid index")
            continue
        elif int(index) > leng - 1:
            print("Invalid index")
            continue
        elif int(index) <= leng - 1:
            return int(index)
        else:
            print("Invalid syntax")
            continue
        

def get_letter(index):
    index = int(index)
    while True:
        word = input(str("Enter a letter: "))
        if word.isupper():
            print("Character must be a lowercase letter!")
            continue
        elif len(word) > 1:
            print("Must be exactly one character!")
            continue
        else:
            """
            list_word = list(initial_word)
            list_word[index] = word
            print ("".join(list_word))
            return list_word
            """
            return word

initial_word = input(str("Enter a word: "))

while True:
    val = get_index(initial_word)
    if val == "no":
        break
    
    else:
        letter = (get_letter(int(val)))
        list_initial_word = list(initial_word)
        list_initial_word[val] = letter
        initial_word = "".join(list_initial_word)
        print(initial_word)
