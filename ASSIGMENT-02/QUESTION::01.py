print("Assignment::02 Question::01")

word = input("Enter the word to be capitalized: ")
word_try = list(word)
count = 0
for i in word:
    count += 1
    if count % 2 == 0:
        app = i.upper()
        print(app, end="")
    else:
        print(i, end="")
