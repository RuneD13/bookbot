import sys
from stats import count_words, count_chars, sort_chars, sort_on

def get_book_text(filepath):
    with open(filepath) as t:
        file_contents = t.read()
    return file_contents



def main():
    n = len(sys.argv) 
    if n != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    word_tally = count_words(book_text)
    #print(word_tally,"words found in the document")
    char_count = count_chars(book_text)
    
    sorted_char_count = sort_chars(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at", sys.argv[1])
    print("----------- Word Count ----------")
    print("Found", word_tally, "total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()