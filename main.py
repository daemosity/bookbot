def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text):
    normalized_chars = text.lower()
    character_count_dict = {}
    for char in normalized_chars:
        if char in character_count_dict:
            character_count_dict[char] += 1
        else:
            character_count_dict[char] = 1
    return character_count_dict

def dict_to_key_val_dict_list(dict):
    key_val_obj_list = []
    for k, v in dict.items():
        obj =  {"key": k, "val": v}
        key_val_obj_list.append(obj)
    return key_val_obj_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    character_count_dict = count_characters(file_contents)
    print(f"Frankenstein has {word_count} words!")
    print(f"Breakdown of characters:")
    print(character_count_dict)

main()