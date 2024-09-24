import argparse
import hashlib
import re

"""
Naming convention
s: split
wd: word
l: list
passwd: password
"""

def jill():
    #opens file and makes file readable
    wdlfile = open('wordlist.txt', 'r') 
    #defines rfile and reads file
    rwdlfile = wdlfile.read()
    #splits file into a list of 
    rwdlsfile = rwdlfile.split('\n')

    #opens file and makes it readable
    passwdfile = open('passwords.txt', 'r')
    #defines reading file and reads file
    rpasswdfile = passwdfile.read()
    #splits file by new lines and colons
    rpasswdsfile = re.split('[:\n]', rpasswdfile)


    a = []
    for x in rwdlsfile:
        print(x)
        # Create a SHA-256 hash object
        sha256_hash = hashlib.sha256(str([x]).encode('utf-8'))
        # Update the hash object with the password bytes
        sha256_hash.update(str([x]).encode('utf-8'))
        
    # Return the hexadecimal representation of the hash
    return print(sha256_hash.hexdigest())

print(jill())

