from stats import get_num_words
from stats import get_char_count
from stats import sort_dict
import sys

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def main():
    #print("initiating booktext...")
    output, text = get_num_words(path)
    char_num = get_char_count(text)
    sorted_dict = sort_dict(char_num)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {output} total words")
    print("----------- Character Count ----------")
    for char in sorted_dict:
        if char.isalpha():
            print(f"{char}: {sorted_dict[char]}")
    return
main()