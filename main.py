from stats import text_count

filepath = "./books/frankenstein.txt"


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book = get_book_text(filepath)
    count = text_count(book)
    print(f"Found {count} total words")


main()

