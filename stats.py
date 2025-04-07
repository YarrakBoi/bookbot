def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read().split()
    return len(file_contents)

def get_num_letters(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
    letters = {}
    
    for letter in file_contents:
        if letter.isalpha():
            if letter.lower() not in letters:
                letters[letter.lower()] = 1
            else:
                letters[letter.lower()] += 1
    
    lettersList = list(letters.items())
    
    return sorted(lettersList, key=lambda item: item[1], reverse=True)
            