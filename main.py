with open('./books/frankenstein.txt', encoding="utf-8") as f:
    file_contents = {"content": f.read(), "name": f.name}


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
    sorted_char_counts = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
    for letter, count in sorted_char_counts.items():
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")

def print_report(file_contents):
    name =file_contents["name"]
    content = file_contents["content"]
    print(f"--- Begin report of {name} ---")
    count_words(content)
    count_letters(content)
    letters_only(letters_dict)
    print("--- End report ---")

print_report(file_contents)
