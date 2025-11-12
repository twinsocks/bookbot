from stats import get_num_words, get_char_freq, sort_char_freq

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)

    word_count = get_num_words(text)
    char_freq = get_char_freq(text)
    sorted_char_freq = sort_char_freq(char_freq)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_freq:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()