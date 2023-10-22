with open('./books/frankenstein.txt', encoding="utf-8") as f:
    file_contents = f.read()

def count_words(content):
    words = len(content.split())
    print(f"{words} found in the document")



letters_dict = {}
def count_letters(content):

    transform_content = content.lower()
    for i in transform_content:
        if i in letters_dict:
            letters_dict[i] += 1
        else: letters_dict[i] = 1
    return letters_dict



def letters_only(char_counts):
    char_list = list(char_counts.keys())
    print(char_list)
    for letter in char_list:
        if letter.isalpha() and letter in letters_dict:
            print(f"The '{letter}' character was found {letters_dict[letter]} times")




def print_report(file_contents):
    print("--- Begin report of books/frankenstein.txt ---")
    count_words(file_contents)
    count_letters(file_contents)
    letters_only(letters_dict)
    print("--- End report ---")

print_report(file_contents)
