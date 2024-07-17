import hashlib
import string
import time
import argparse


def doStuff(filein, fileout):
    with open(filein, mode = "r", encoding='utf-8') as fin, open(fileout, mode ='w', encoding = 'utf-8') as fileout:
        hashes = fin.read().split('\n')
        hashes.pop()
        print(hashes)

        chars = string.ascii_lowercase + string.digits

        flag = False
        print('start')
        start_time = time.time()
        for first in chars:
            for second in chars:
                for third in chars:
                    for fourth in chars:
                        for fifth in chars:
                            text = f"{first}{second}{third}{fourth}{fifth}"
                            result = hashlib.md5(text.encode()).hexdigest()
                            if result in hashes:
                                hashes.remove(result)
                                print(f"answer is : {text}")
                                fileout.write(text)
                                fileout.write('\n')
                                if (len(hashes) == 0):
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



        end_time = time.time()
        print(f"Duration: {end_time-start_time} second")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest = 'filein', help = 'input file')
    parser.add_argument('--o', dest = 'fileout', default = 'ex2_hash.txt', help = 'file out')
    
    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout
    doStuff(filein, fileout)