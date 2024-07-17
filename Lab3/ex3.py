import argparse
import random
import string
import hashlib
import time

def doStuff(filein, fileout1, fileout2):
    with open(filein, mode = 'r', encoding='utf-8') as fin, open(fileout1, mode = 'w', encoding='utf-8') as foutplain, open(fileout2, mode = 'w', encoding='utf-8') as fouthash:
        hashes = fin.read().split('\n')
        hashes.pop()
        print(hashes)

        hash_arr = []

        for i in range(len(hashes)):
            hashes[i] += random.choice(string.ascii_lowercase)
            foutplain.write(hashes[i]+ '\n')
            fouthash.write(hashlib. md5(hashes[i].encode()).hexdigest() + '\n')
            hash_arr.append(hashlib.md5(hashes[i].encode()).hexdigest())
        print(hash_arr)

        chars = string.ascii_lowercase + string.digits
        flag = False
        print('start')
        start_time = time.time()
        for first in chars:
            for second in chars:
                for third in chars:
                    for fourth in chars:
                        for fifth in chars:
                            for sixth in chars:
                                text = f"{first}{second}{third}{fourth}{fifth}{sixth}"
                                result = hashlib.md5(text.encode()).hexdigest()
                                if result in hash_arr:
                                    hash_arr.remove(result)
                                    print(f"answer is : {text}")
                                    if (len(hash_arr) == 0):
                                        flag = True
                                if flag:
                                    break
                            if flag:
                                break
                        if flag:
                            break
                    if flag:
                        break
                if flag:
                    break
            if flag:
                break
        end_time = time.time()
        print(f"Duration: {end_time-start_time} second")



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest = 'filein', help = 'input file')
    parser.add_argument('--o1', dest = 'fileout1', default = 'plain6.txt', help = 'file out for plain')
    parser.add_argument('--o2', dest = 'fileout2', default = 'salted6.txt', help = 'file out for hash')

    
    args = parser.parse_args()
    filein = args.filein
    fileout1 = args.fileout1
    fileout2 = args.fileout2
    doStuff(filein, fileout1, fileout2)