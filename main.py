def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(F"{word_count} words found in the document")
    
    lower_text = text.lower()
    character_count = count_characters(lower_text)

    report = report_func(character_count)
    for item in report:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    return wordcount

def count_characters(lower_text):
    character_count = {}
    for character in lower_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_on(dict):
    return dict["num"]
    
def report_func(character_count):
    char_list = []
    for char, count in character_count.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
        char_list.sort(reverse=True, key=sort_on)
    return char_list

main()
