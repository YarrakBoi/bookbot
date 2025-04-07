from stats import get_num_words, get_num_letters
import sys

def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    wordCounter = get_num_words(f"{sys.argv[1]}")
    #print(f"Found {wordCounter} total words")
    letterCounter = get_num_letters(f"{sys.argv[1]}")
    #print(letterCounter)
    
    bookbot = "============ BOOKBOT ============\n"
    analyzing = f"Analyzing book found at {sys.argv[1]}...\n"
    wordCount = f"----------- Word Count ----------\nFound {wordCounter} total words\n"
    charCounter = f"--------- Character Count -------\n"
    end = "============= END ==============="
    
    counter = ""
    for k, v in letterCounter:
        counter += f"{k}: {v}\n"
        
    print(bookbot + analyzing + wordCount + charCounter + counter + end)
    
main()