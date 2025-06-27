def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    char_dict = {}
    words = text.lower()
    for c in words:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def char_sort(char_dict):
    sorted_char_dict = []
    for i in char_dict:
        sorted_char_dict.append({"char": i, "num": char_dict[i]})
    sorted_char_dict.sort(reverse=True, key=sort_on)
    return sorted_char_dict

def sort_on(item):
    return item["num"]