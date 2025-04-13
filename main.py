from stats import wordcount, charcount, sort_chars
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    # Exit the program
    sys.exit(1)

clarg1 = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = clarg1
    string = get_book_text(filepath)

    # Get statistics
    num_words = wordcount(string)
    chars_dict = charcount(string)
    sorted_chars = sort_chars(chars_dict)

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Print character counts (alphabetic only)
    for char_data in sorted_chars:
        char = char_data["char"]
        count = char_data["num"]
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()
