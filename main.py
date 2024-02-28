def main():
    book_path = "books/frankenstein.txt"
    book = load_book(book_path)
    book_words_count = word_count(book)
    book_letters = letter_count(book)
    d_list = dict_list(book_letters)
    d_list.sort(reverse=True, key=key_sort)
    
    print(f"--- Begin report on {book_path} ---")
    print()
    print(f"{book_words_count} words found in document")
    print()
    for d in d_list:
        L = d["letter"]
        C = d["count"]
        if L.isalpha():
            print(f"The '{L}' character was found '{C}' times.")
        else:
            pass
    print()
    print("--- End report ---")
    

def load_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def word_count(text):
    stext = text.split()
    counter = 0
    for i in range(0, len(stext)):
        counter += 1
    return counter

# returns a dictionary
def letter_count(text):
    stext = text.split()
    letters = {}
    for word in stext:
        for letter in word:
            letter = letter.lower()
            if letter in letters:
                letters[f'{letter}'] += 1
            else:
                letters[f'{letter}'] = 1
    return letters

#converts a dictionary into a list of dictionaries
def dict_list(dict):
    r_list = []
    for entry in dict:
        temp_dict = {"letter": "", "count": ""}
        temp_dict["letter"] = entry
        temp_dict["count"] = dict[entry]
        r_list.append(temp_dict)

    return r_list

#key for the .sort() method      
def key_sort(dict):
    return dict["count"]



    

main()