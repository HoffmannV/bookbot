#!/usr/bin/env python3

import sys, getopt

def main(argv): 
   input_file = ''
   output_file = ''
   report = ''

   try:
       opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
       
       for opt, arg in opts:
           if opt == '-h':
               print ('usage: test.py -i <inputfile> -o <outputfile>')
               sys.exit()
           elif opt in ("-i", "--ifile"):
               with open(arg) as f:
                   input_file=arg.split('/')
                   file_contents = f.read()
                   report = generate_report(file_contents, input_file[len(input_file)-1])

           elif opt in ("-o", "--ofile"):
               output_file = arg
               f = open(output_file, "w")
               f.write(report)
               f.close()
               print(f"The report has been generated into the file {output_file}")

       if output_file == '':
           print(report)

   except getopt.GetoptError:
       print("usage: test.py -i <inputfile> -o <outputfile>")

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

def generate_report(text, name):
    word_count = count_words(text)
    char_dict = dict(sorted(count_chars(text).items(), key=lambda x:x[1], reverse=True))

    report = f"--- Begin report of books ---\n{word_count} words found in the document\\{name}\n"
    for char in char_dict.keys():
        if char.isalpha():
            report += f"\nThe \'{char}\' character was found {char_dict[char]} times"
    
    report += "\n--- End report ---"
    return report


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
