import sys
from stats import get_num_words, count_characters, dict_to_key_val_dict_list, filter_key_val_dict_list_to_alphas

def print_report(filepath, word_count, character_count_obj_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_obj in character_count_obj_list:
        
        print(f"{char_obj['key']}: {char_obj['val']}")
    print("============= END ===============")

def main(): 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")  
        sys.exit(1)
    
    filepath = f"{sys.argv[1]}"
    with open(filepath) as f:
        file_contents = f.read()
    
    word_count = get_num_words(file_contents)
    character_count_dict = count_characters(file_contents)
    character_count_list= dict_to_key_val_dict_list(character_count_dict)
    sorted_alpha_count_list = filter_key_val_dict_list_to_alphas(character_count_list)
    
    print_report(filepath, word_count, sorted_alpha_count_list)
    
main()