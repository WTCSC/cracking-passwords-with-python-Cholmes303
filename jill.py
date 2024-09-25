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
    
    # List of usernames for each hash
    usernames = []
    
    # List for hashes that are made to compare
    keys = []
    
    # List for hashes in file
    passwords = []

    #list of hashes that match
    output = []
        
    line = 0
        
    # Loops through each line in file with passwords and has a length count
    for y in range(0, (length * 2)):
        
        # If length is divisible by 2 it puts that line of contents into the username list
        if y % 2 == 0:
            usernames.append(rpasswdsfile[y])
        
        # If length is not divisible by 2 it puts that line of contents into the passwords list
        else:
            passwords.append(rpasswdsfile[y])
    
    # Loops through strings in passswords list
    for h in passwords:
        
        # Since usernames are on even lines this allows the function to find the even lines (usernames) and print them
        line += 1
        
        # Loops through strings in keys list
        for k in rwdlsfile:
        
            # Hashes x in rwdlsfile 
            sha256_hash = hashlib.sha256(str(k).encode('utf-8'))
        
            # Puts hash into keys array
            hashd = sha256_hash.hexdigest()
            
            # Compares string in keys (k) to string in passwords (h)
            if h == hashd:
                
                output += ['{0:02}:{1:02}'.format(usernames[(line - 1)], k)]
            print(output)

    return output
print(jill())
