import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import number_of_words
from stats import character_count
from stats import sorted_dictionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main ():
    path_to_book = sys.argv[1]
    num_words = number_of_words(get_book_text(path_to_book))
    num_characters = character_count(get_book_text(path_to_book))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars = sorted_dictionary(num_characters)
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")
    
    
    

    
main()