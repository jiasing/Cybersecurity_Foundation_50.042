#!/usr/bin/env python3
# ECB plaintext extraction skeleton file for 50.042 FCS

import argparse

def getInfo(headerfile):
    with open(headerfile, mode='rb') as fin:
        info = fin.read()
    fin.close()
    return info

def extract(infile,outfile,headerfile):
    header_info = getInfo(headerfile)

    with open(infile, 'rb') as fin, open(outfile, 'wb') as fout:
        fin.read(len(header_info))
        fout.write(header_info)
        fout.write(b'\n')
        fout.write(b'\n')
        fin.read(1)        

        first = fin.read(8)
        fout.write(b'00000000')

        while True:
            curr = fin.read(8)
            if curr == b'':
                break
            if curr == first:
                fout.write(b'00000000')
            else:
                fout.write(b'11111111')

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Extract PBM pattern.')
    parser.add_argument('-i', dest='infile',help='input file, PBM encrypted format')
    parser.add_argument('-o', dest='outfile',help='output PBM file')
    parser.add_argument('-hh', dest='headerfile',help='known header file')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    headerfile=args.headerfile

    print('Reading from: %s'%infile)
    print('Reading header file from: %s'%headerfile)
    print('Writing to: %s'%outfile)

    success=extract(infile,outfile,headerfile)