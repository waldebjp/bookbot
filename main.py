def main():
    book_path = "books/frankenstein.txt"
    book = "frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_dict = get_num_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(characters_dict)
    print(f"---  Begining report of text: {book}  ---")
    print(f"*   There are {num_words} words in the text")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("---  Ending report  ---")

#Get the path of the text
def get_book_text(path):
    with open(path) as f:
        return f.read()

#Get the number of words on the text
def get_num_words(text):
    words = text.split()
    return len(words)

#Get the number of characters on the text and put the in a dictionary
def get_num_characters(text):
    characters_dict = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in characters_dict:
            characters_dict[lowered] += 1
        else:
            characters_dict[lowered] = 1
    return characters_dict

#Sort dictionary based on key, in this case num
def sort_on(dict):
    return dict["num"]

#Sorts the list by using the sort_on function above
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()