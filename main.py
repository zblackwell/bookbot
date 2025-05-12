from stats import get_num_words
from stats import character_count
from stats import book_report
import sys

def get_book_test (path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main ():
    try:
        file_contents = get_book_test(sys.argv[1])
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    total_words = get_num_words(file_contents)
    character_dict = character_count(file_contents)
    report = book_report(total_words,character_dict,sys.argv[1])
    for item in report:
        print(item)
    #print(f"{total_words} words found in the document")
    #print(character_dict)


main()