from stats import get_num_words, get_num_char, char_sort
import sys


def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        num_chars = get_num_char(text)
        num_chars_sorted = char_sort(num_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in num_chars_sorted:
            if i["char"].isalpha():
                print(f"{i['char']}: {i['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
