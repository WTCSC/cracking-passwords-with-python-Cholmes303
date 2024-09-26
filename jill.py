import argparse
import hashlib
import re

"""
Naming convention
r: read
s: split
wd: word
l: list
x: line in file
p: username:password output
len: length
passwd: password
"""

# Function used to crack hashed passwords by comparing a list of words to hashed passwords
def jill(passwordtxt, wordlisttxt):
    
    # Defines file with words to compare hashes as wdlfile, opens file, and makes file readable
    wdlfile = open(wordlisttxt, 'r') 
    
    # Defines rwdlfile and reads file
    rwdlfile = wdlfile.read()
    
    # Defines rwdlsfile and splits file into a list of strings, each line in the file being a string
    rwdlsfile = rwdlfile.split('\n')

    # Defines file with hashed passwords as passwdfile, opens file, and makes it readable
    passwdfile = open(passwordtxt, 'r')
    
    # Reads length of file (# of lines) and closes
    length = len(passwdfile.readlines())
    
    # Re-opens file and makes it readable again
    lenpasswdfile = open(passwordtxt, 'r')
    
    # Defines rpasswdfile and reads file
    rpasswdfile = lenpasswdfile.read()
    
    # Splits file by new lines and colons
    rpasswdsfile = re.split('[:\n]', rpasswdfile)
    
    # List of usernames for each hashed password
    usernames = []
    
    # List for hashes in file of usernames and hashed passwords
    passwords = []

    # List of the username and word that matched hashed password
    output = []

    # Defines line to be used to find the username or password within file    
    line = 0
        
    # Loops through each line in file with usernames and passwords to sort each into their respective list
    for x in range(0, (length * 2)):
        
        # If length is divisible by 2 it puts that line of contents into the username list
        if x % 2 == 0:
            usernames.append(rpasswdsfile[x])
        
        # If length is not divisible by 2 it puts that line of contents into the passwords list
        else:
            passwords.append(rpasswdsfile[x])
    
    # Loops through the hashed passwords in the passwords list
    for h in passwords:
        
        # Since usernames are on even lines this allows the function to find the even lines (usernames) and put them into the output
        line += 1
        
        # Loops through the list of words that are going to be hashed and compared
        for wd in rwdlsfile:
        
            # Defines sha256_hash and hashes each line/word in rwdlsfile 
            sha256_hash = hashlib.sha256(str(wd).encode('utf-8'))
        
            # Defines hashd and puts the hashed word into hexadecimal values
            hashd = sha256_hash.hexdigest()
            
            # Compares the hashed string in rwdsfile (hashd) to hashed string in passwords (h)
            if h == hashd:
                
                # Puts the words that match the hashes in passwords into an output list in usernames:password format. 
                # The variable k is used as this is the unhashed value. 
                # [(line - 1)] is used to pull the correct username for each password.
                output += ['{0:02}:{1:02}'.format(usernames[(line - 1)], wd)]
    
    # Returns list of usernames and words that matched
    return output

def main():

    # Description of the program
    parser = argparse.ArgumentParser(description='Crack passwords with two files')
    
    # Adds two arguments that can be used to compare two files to crack password
    parser.add_argument('passwordtxt', help='File with passwords that need to be cracked') 
    parser.add_argument('wordlisttxt', help='File with words to try')

    args = parser.parse_args()

    # Adds the two arguments defined to the password cracking function
    arguments = jill(args.passwordtxt, args.wordlisttxt)
    
    # Loops through the arguments in password cracking function and prints matching usernames and passwords
    for p in arguments:
        print(p)

if __name__ == "__main__":
    main()