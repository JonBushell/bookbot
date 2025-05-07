def number_of_words(book_as_text):
    word_count = len(book_as_text.split())
    return word_count

def character_count(book_as_text):
    character_dict = {}
    for char in book_as_text.lower():
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

