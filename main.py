def get_book_text(x):
    with open(x) as f:
        file_contents = f.read()
    return file_contents

def main():
    x = count()
    print(f"{x} words found in the document")

def count():
    words = get_book_text("books/frankenstein.txt").split()
    word_count = len(words)
    return word_count

main()