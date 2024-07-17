import sys
import argparse

def doStuff(filein):
    with open(filein, mode = "r", encoding='utf-8') as fin:
        text = fin.read()
        
        curr_word = ''
        list_of_words = {}
        print(text + '\n')
        text =  swap_chars(text, 'Y', 'I') 
        text =  swap_chars(text, 'Q', 'A')
        text =  swap_chars(text, 'J', 'N')
        text =  swap_chars(text, 'B', 'L') 
        text =  swap_chars(text, 'D', 'S')      
        print(text)


        for letter in text:
            if letter == ' ':
                if curr_word not in list_of_words:
                    list_of_words[curr_word] = 1
                    curr_word = ''
                else:
                    list_of_words[curr_word] += 1
                    curr_word = ''
            else:
                curr_word += letter

        sorted_dict = dict(sorted(list_of_words.items(), key=lambda item: len(item[0])))
        print(sorted_dict.keys())

# given a -> b and x -> y, if we say that all every a shld be map to y, then every x shld be mapped to b.
def swap_chars(text, char1, char2):
    swap_table = str.maketrans(char1 + char2, char2.lower() + char1)
    return text.translate(swap_table)

#our main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="filein", help="input file")

    args = parser.parse_args()
    filein = args.filein

    changed = []
    doStuff(filein)
