def get_num_words(path_file):
    with open(path_file) as f:
        #print(f"{path_file} : file opened")
    # f is a file object
        file_contents = f.read()
        #print("file content was read")
    
    words = file_contents.split()
    count = len(words)
    return count, file_contents
def get_char_count(text):
    chars = {}
    l_text = text.lower()
    for char in l_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars
def sort_dict(dict_uns):
    # Sort the dictionary items by value in reverse order
    sorted_items = sorted(dict_uns.items(), key=lambda item: item[1], reverse=True)
    
    # Create a new dictionary from the sorted items
    sorted_dict = dict(sorted_items)
    
    return sorted_dict