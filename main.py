from stats import number_of_words
from stats import character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main ():
    num_words = number_of_words(get_book_text("books/frankenstein.txt"))
    num_characters = character_count(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    print (num_characters)

    
main()