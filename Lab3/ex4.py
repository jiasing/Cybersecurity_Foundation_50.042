import argparse
import string
import hashlib
import itertools
import time

def doStuff(filein, fileout):
    with open(filein, mode = 'r', encoding='utf-8') as fin, open(fileout, mode = 'w', encoding='utf-8') as fout:
        hashes = fin.read().split('\n')
        hashes = hashes[:-3]

        chars = string.ascii_lowercase + string.digits

        print(f"we're at i = 7")
        perms = itertools.permutations(chars, 7)

        for possible_hash in perms:
            value = ''.join(possible_hash)
            result = hashlib.md5(value.encode()).hexdigest()
            if result in hashes:
                fout.write(result + " : " + value + '\n')

        print('done')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest = 'filein', help = 'input file')
    parser.add_argument('--o', dest = 'fileout', default = 'ex4answers_7char.txt', help = 'file out')

    
    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout
    doStuff(filein, fileout)