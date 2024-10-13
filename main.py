def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the text")
    characters_dict = get_num_characters(text)
    print(f"The list of characters in the text is:  {characters_dict}")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
characters_dict = {}

def get_num_characters(text):
    characters_dict = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in characters_dict:
            characters_dict[lowered] += 1
        else:
            characters_dict[lowered] = 1
    return characters_dict


main()