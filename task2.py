import string

def unique_words(book):
    
    words = book.lower().translate(str.maketrans("", "", string.punctuation)).split()
    
    return set(words)

def count_the_article(book):
    # Load the list of common words
    with open("20k.txt", "r") as f:
        common_words = f.read().splitlines()
    
    words = book.lower().translate(str.maketrans("", "", string.punctuation)).split()
    
    count = 0
    for word in words:
        if word in common_words:
            count += 1
    return count

def sorted_words(book):
    
    words = book.lower().translate(str.maketrans("", "", string.punctuation)).split()
    # Sort the words based on character count
    sorted_words = []
    for word in words:
        for i, sw in enumerate(sorted_words):
            if len(word) > len(sw):
                sorted_words.insert(i, word)
                break
            else:
                sorted_words.append(word)

    return sorted_words

def character_word_count(book):
    
    words = book.lower().translate(str.maketrans("", "", string.punctuation)).split()
    # Create a dictionary with words as keys and character count as values
    char_count = {}
    for word in words:
        char_count[word] = len(word)
    return char_count

def starts_with_vow(book):
    
    words = book.lower().translate(str.maketrans("", "", string.punctuation)).split()
    # Count the number of words that start with a vowel
    count = 0
    vowels = ("a", "e", "i", "o", "u")
    for word in words:
        if word[0] in vowels:
            count += 1
    return count

def rare_words(book):
    # Load the list of common words
    with open("20k.txt", "r") as f:
        common_words = set(f.read().splitlines())

    
    words = book.lower().translate(str.maketrans("", "", string.punctuation)).split()
    # Find the rare words in the book
    rare_words = []
    for word in words:
        if word not in common_words:
            rare_words.append(word)
    return rare_words

def unused_words(books):
    with open("20k.txt") as f:
        common_words = set(word.strip().lower() for word in f)
    
    unused_words = set(common_words)
    for book in books:
        with open(book) as f:
            book_words = set(word.strip().lower() for word in f)
        unused_words -= book_words
    
    return list(unused_words), len(unused_words)