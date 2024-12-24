def count_words(text: str) -> int:
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text: str) -> dict:
    normalized_chars = text.lower()
    character_count_dict = {}
    for char in normalized_chars:
        if char in character_count_dict:
            character_count_dict[char] += 1
        else:
            character_count_dict[char] = 1
    return character_count_dict

def dict_to_key_val_dict_list(dict: dict) -> list:
    key_val_obj_list = []
    for k, v in dict.items():
        obj =  {"key": k, "val": v}
        key_val_obj_list.append(obj)
    return key_val_obj_list

def sort_on_dict_value(d: dict) -> int:
    return d['val']

def filter_key_val_dict_list_to_alphas(key_val_list: list) -> list:
    filtered_character_count_list = [obj for obj in key_val_list if obj['key'].isalpha()]
    filtered_character_count_list.sort(reverse=True, key=sort_on_dict_value)
    return filtered_character_count_list

def print_report(filepath, word_count, character_count_obj_list):
    print(f"----- Report on {filepath} -----")
    print()
    print(f"{filepath.removeprefix('books/').removesuffix('.txt').title()} comprises of {word_count} words")
    print()
    print(f"Breakdown of alpha characters:")
    for char_obj in character_count_obj_list:
        
        print(f"{char_obj['key']} appears {char_obj['val']} times")
    
    print()
    print("----- End Report -----")

def main():
    filepath = "books/frankenstein.txt"
    
    with open(filepath) as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    character_count_dict = count_characters(file_contents)
    character_count_list= dict_to_key_val_dict_list(character_count_dict)
    sorted_alpha_count_list = filter_key_val_dict_list_to_alphas(character_count_list)
    
    print_report(filepath, word_count, sorted_alpha_count_list)
    
main()