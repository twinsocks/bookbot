from stats import get_num_words, get_char_freq

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    
    char_freq = get_char_freq(text)
    print(char_freq)

main()