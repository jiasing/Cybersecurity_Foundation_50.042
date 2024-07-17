import sys
import argparse
import matplotlib.pyplot as plt

def doStuff(filein, fileout):
    with open(filein, mode = "r", encoding='utf-8') as fin:
        text = fin.read()

    freq_count = {} 
    for letter in text:
        if letter in freq_count:
            freq_count[letter] += 1
        else:
            freq_count[letter] = 1
    #sort dictionary in descending order based on frequency of usage of each character        
    freq_count = dict(sorted(freq_count.items(), key=lambda item: item[1], reverse=True))
    freq_count.pop(' ') #remove space because spaces are left unmapped.


    #list of each char sorted in descending order of use rate, excluding spaces.
    initial_rank = list(freq_count.keys()) 
    #list of each alphabet sorted in descending order of use rate
    descending_list = ['E','A','R','I','O','T','N','S','L','C','U','D','P','M','H','G','B','F','Y','W','K','V','X','Z','J','Q']
    

    #map top 26 most used characters in ciphertext based on frequency analysis. NOTE: 'P' in ciphertext is UNMAPPED! 
    for i in range(len(descending_list)):
         text = translate_text(text, initial_rank[i], descending_list[i] )


    swaps = {}
    swaps['e'] = 'E'    #ase --> THE
    swaps['a'] = 'T'    #ase --> THE
    swaps['s'] = 'H'    #ase --> THE
    swaps['w'] = '.'    #last character of the text should be fullstop
    swaps['i'] = 'A'    # since r is mapped to I, the other single character word 'i' should map to A 
    swaps['r'] = 'I'    # many sentences start with r, it could be I
    swaps['k'] = ','    # "coooooadk” and “coooad" suggests the k should be a comma
    swaps['n'] = 'S'    # “HEARTn” --> “HEARTS”
    swaps['x'] = 'V'    # “HAxE” --> “HAVE”
    swaps['b'] = 'W'    # “bHAT” --> “WHAT”
    swaps['v'] = 'B'    # “vETTER” --> “BETTER” 
    swaps['c'] = 'L'    # “acc” --> “ALL”
    swaps['f'] = 'F'    # “fOl” --> “FOR”
    swaps['o'] = 'O'    # “fOl” --> “FOR”
    swaps['l'] = 'R'    # “fOl” --> “FOR”
    swaps['p'] = 'M'    # “TIpE” --> “TIME”
    swaps['t'] = 'N'    # “LOOOOOtd” --> “LOOOOONG”
    swaps['d'] = 'G'    # “LOOOOOtd” --> “LOOOOONG”
    swaps['u'] = 'D'    # “BOTHEREu” --> “BOTHERED”
    swaps['h'] = 'Y'    # “MhSELF” --> “MYSELF”
    swaps['m'] = 'C'    # “FRANmHISE” --> “FRANCHISE”   
    swaps['g'] = 'U'    # “THROgGHOgT” --> “THROUGHOUT”  
    swaps['j'] = 'X'    # “EjyECT” --> “EXPECT”
    swaps['z'] = 'K'    # “zNOW” --> “KNOW”
    swaps['q'] = 'J'    # “qOURNEY” --> “JOURNEY”
    swaps['P'] = 'Z'    # "POMPIE" --> "ZOMBIE"
    swaps['y'] = 'P'    # “EjyECT” --> “EXPECT”

    text = swap_text(text,swaps)
    
    with open(fileout, mode = "w", encoding='utf-8') as fout:
        fout.write(text)
    #functions below were used to print out new texts and lists for decoding purposes. 
    # get_all_words(text)
    # print()
    # print(text)
    # print()
    # print(count_words(text))

#prints out a dictionary where keys = unique words in text and value = number of appearance in the text.
def count_words(text):
    word_list = list(text.split(" "))
    word_dict = {}
    for i in word_list:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1]))
    return word_dict


#translates all char1 to char2. Used to translate our initial ciphertext based on frequency analysis.
def translate_text(text, char1, char2):
    translation = str.maketrans(char1, char2.lower())
    text = text.translate(translation)
    return text

#Function to swap text based on key-value pair in dictionary.
#Throws error if we're mapping to a character we've already previously identified.
def swap_text(text, swaps):
    corrected = [] 
    for char1,char2 in swaps.items():
        if char2 not in corrected:
            text = swap_text_actual(text, char1,char2)
            corrected.append(char2)
        else:
            print(corrected)
            print(f"Cant swap {char1} and {char2}")
            exit()
    return text

#helper function used by swap_text function
def swap_text_actual(text, char1, char2):
    translation = str.maketrans(char1+char2, char2.upper()+char1)
    text = text.translate(translation)
    return text

#returns list of all unique words in the text
def get_all_words(text):
    word_list = list(set(text.split(" ")))
    word_list = sorted(word_list, key = lambda x: len(x))
    print(word_list)
    return word_list


#our main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="filein", help="input file")
    parser.add_argument("--o", dest = "fileout", help = "output file", default='solution.txt')

    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout
    doStuff(filein,fileout)