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

# You may set up functions like this, or you can do it your own way

def encrypt(filepath, message):
    # add code to encrypt a message and write the encryption to a text file
    chars = list(set(message))
    key = {}
    for index in range(len(chars)):
        key[chars[index]] = chars[(index + 1) % len(chars)]
    keytext = ""
    for k in key.keys():
        keytext += k + key[k]
    newmsg = ""
    for char in message:
        newmsg += key[char]

    with open(filepath, "w") as f:
        f.write(keytext)
        f.write("\n\n\n")
        f.write(newmsg)



def decrypt(infile, outfile):
    # add code to open a text file and decrypt the message
    with open(infile, "r") as f1:
        intext = f1.read()
    components = intext.split("\n\n\n")
    keytext = components[0]
    msgtext = components[1]

    decipher = {}
    for index in range(0, len(keytext), 2):
        decipher[keytext[index + 1]] = keytext[index]
    
    original = ""
    for char in msgtext:
        original += decipher[char]

    with open(outfile, "w") as f2:
        f2.write(original)


if __name__ == "__main__":
    with open("message.txt", "r") as f:
        text = f.read()
    filename = "encrypted.txt"
    encrypt(filename, text)
    outfile = "decrypted.txt"
    decrypt(filename, outfile)
    
    text1 = open("message.txt").readlines()
    text2 = open("decrypted.txt").readlines()
    print(text1 == text2)



