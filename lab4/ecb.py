#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.042 FCS

from present import *
import argparse
import math

nokeybits=80
blocksize=64


def ecb(infile,outfile,key,mode):

    with open(infile, mode='rb') as fin, open(outfile, mode='wb') as fout:
        data = fin.read()
        key_int = int(key)
        block_length = math.ceil(len(data) / 8)
        int_value = int.from_bytes(data, byteorder='big')

        final = 0

        if mode.lower() == 'e':
            for i in range(block_length - 1, -1, -1):
                curr_block = (int_value >> i * blocksize) & 0xffffffffffffffff
                final = (final <<blocksize) | present(curr_block, key_int)
       
        else:   #do decryption
            for i in range(block_length - 1, -1, -1):
                curr_block = (int_value >> i * blocksize) & 0xffffffffffffffff
                final = (final <<blocksize) | present_inv(curr_block, key_int)

        final = final.to_bytes((final.bit_length() + 7) // 8, 'big')
        fout.write(final)

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode', choices=['e','d'] )

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode = args.mode
    ecb(infile, outfile, keyfile, mode)