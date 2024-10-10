import sys

def main(): 
    with open("books/frankenstein") as f:
        file_contents = f.read()
        print(generate_report(file_contents))

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower().replace(' ', '')
    char_dict = dict()
    
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def generate_report(text):
    word_count = count_words(text)
    char_dict = dict(sorted(count_chars(text).items(), key=lambda x:x[1], reverse=True))

    report = f"--- Begin report of books ---\n{word_count} words found in the document\n"
    for char in char_dict.keys():
        if char.isalpha():
            report += f"\nThe \'{char}\' character was found {char_dict[char]} times"
    
    report += "\n--- End report ---"
    return report


if __name__ == "__main__":
    sys.exit(main())
