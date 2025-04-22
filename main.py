def get_book_text(x):
    with open(x) as f:
        file_contents = f.read()
    return file_contents

def main():
  try:
    print(get_book_text("books/frankenstein.txt"))
  except FileNotFoundError:
     print("File could not be found")
     
main()
