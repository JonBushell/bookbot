from stats import number_of_words
from stats import character_count
from stats import sorted_dictionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main ():
    num_words = number_of_words(get_book_text("books/frankenstein.txt"))
    num_characters = character_count(get_book_text("books/frankenstein.txt"))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars = sorted_dictionary(num_characters)
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")
    
    
    

    
main()