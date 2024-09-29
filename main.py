def main(book_path):

    file_content = file_contents(book_path)

    print(f"--- Begin report of {book_path} ---")
    
    words = count_words(file_content)
    
    print(f"{words} wrods found in the document")
    
    characters = count_character(file_content)
    alphabets = check_alpha(characters)
    for alphabet in alphabets:
        print("The '"+ alphabet["name"]+ "' character was found ", alphabet["num"]," times")
    print("--- End report ---")



# A function for making a list of dictionaries from one dictonary and sorting
# e:g {'e': 123, 'i': 23, 'b': 54}
# return [{'name': 'e', 'num': 123}, {'name': 'b', 'num':54}, {'name': 'i', 'num': 23}]
# sorted and seprated dict
def check_alpha(dict):
    alphabets = []
    for alpha in dict:
        alpha_dict = {}
        if alpha.isalpha():
            alpha_dict["name"] = alpha
            alpha_dict["num"] = dict[alpha]
            alphabets.append(alpha_dict)
    alphabets.sort(reverse=True, key=sort_on)
    return alphabets

# A function for simply returning the value of 'key' in dictionary.
# In this case the 'key' is "num"
def sort_on(dict):
    return dict["num"]

# A function for reading the content of a file 
def file_contents(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

# A function for simply count the number of words in a file
def count_words(string):
    words = string.split()
    counter = len(words)
    return counter

# A function for counting all the character and how many times have the been used
def count_character(string):
    sentence = string.lower()
    character = {}
    for char in sentence:
        if char in character:
            character[char] += 1
        else:
            character[char] = 1
    return character

main("books/frankenstein.txt")
