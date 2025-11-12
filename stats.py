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


        
