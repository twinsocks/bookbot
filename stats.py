def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_freq(text):
    char_freq = {}
    ltext = text.lower()
    for char in ltext:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq

def sort_char_freq(char_freq):
    sorted_char_freq = []
    for char in char_freq:
        if char.isalpha():
            sorted_char_freq.append({"char": char, "num": char_freq[char]},)
    def sort_on(item):
        return item["num"]

    sorted_char_freq.sort(key=sort_on, reverse=True)
    return sorted_char_freq