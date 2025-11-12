def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words():
    text = get_book_text("./books/frankenstein.txt")
    words = text.split()
    print(f"Found {len(words)} total words")