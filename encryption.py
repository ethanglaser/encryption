# This project seeks to be able to encrypt and decrypt messages
# The implementation of this project is up to the individual
# Example: Add a key at the top of the file where you write a letter followed by its substitute
#      if we wanted to write a message "hello" and encrypt h with a, e with b, etc. then the key
#      may look like:  haeblcod (encrpyt h as a, e as b, l as c, o as d)
#      then then encrypted message would be: abccd
#      The entire contents of the file encrypted this way may look like the following:
'''
haeblcod
abccd
'''
# This project is meant to be flexible, so come up with a way to encrypt a message, as well as decrypting the encrypted message
# Start off with a basic encryption and work your way up to something complicated!

# You may set up functionz like this, or you can do it your own way

def encrypt(filepath, message):
    # add code to encrypt a message and write the encryption to a text file
    pass

def decrypt(filepath):
    # add code to open a text file and decrypt the message
    pass

if __name__ == "__main__":
    message = ""
    filename = ""
    encrypt(message, filename)

