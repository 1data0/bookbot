import sys
from stats import get_num_words, get_num_chars, sort_num_chars


def get_book_text(path: str) -> str:
    s = ""
    with open(path) as f:
        s = f.read()
    return s


def main():

    args = sys.argv

    if not len(args) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = args[1]

    text = get_book_text(path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_num_chars = sort_num_chars(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for x in sorted_num_chars:
        if x["name"].isalpha:
            print(f"{x['name']}: {x['value']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
