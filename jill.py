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
    # Opens file and makes file readable
    wdlfile = open('wordlist.txt', 'r') 
    # Defines rfile and reads file
    rwdlfile = wdlfile.read()
    # Splits file into a list of
    rwdlsfile = rwdlfile.split('\n')

    # Opens file and makes it readable
    passwdfile = open('passwords.txt', 'r')
    # Reads length of file (lines)
    length = len(passwdfile.readlines())
    # Re-opens file and makes it readable
    lpasswdfile = open('passwords.txt', 'r')
    # Defines reading file and reads file
    rpasswdfile = lpasswdfile.read()
    # Splits file by new lines and colons
    rpasswdsfile = re.split('[:\n]', rpasswdfile)
    print(rpasswdsfile)
    usernames = []
    keys = []
    passwords = []
    # Loops through each line of code and hashes each line
    for x in rwdlsfile:
        # Hashes x in rwdlsfile (when using str(x) you added [] around the x inside the () making 123456 become ['123456']
        sha256_hash = hashlib.sha256(str(x).encode('utf-8'))
        # converts line in file to hash
        keys.append(sha256_hash.hexdigest())

        # Loops through each line of rpasswdsfile
    for y in range(0, (length * 2)):

        if y % 2 == 0:
            usernames.append(rpasswdsfile[y])
        else:
            passwords.append(rpasswdsfile[y])

        


    print(usernames)
    print(passwords)
    return

print(jill())

