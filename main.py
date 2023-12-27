with open("books/frankenstein.txt") as f:
    content = f.read()
    words = content.split()
    num_words = len(words)
    print(f"The file {f.name} has about {num_words} words.")
    letters = {}
    for word in words:
        lower_word = word.lower()
        for letter in lower_word:
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1
    for letter in letters.items():
        print(f"the {letter[0]} character appears: {letter[1]}")
