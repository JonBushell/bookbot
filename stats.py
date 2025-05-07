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

def sorted_dictionary(character_dict):
    sorted_list = []      #creating an empty list to make a list of dictionaries  
    for char in character_dict:
        count = character_dict[char]
        char_dict = {"char": char, "num": count}
        sorted_list.append(char_dict)
    #List created, Will now handle sorting of the list in descending order
    def sort_on(dict):
        return dict["num"]

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

