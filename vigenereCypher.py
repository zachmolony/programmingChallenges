import string
alpha = string.ascii_uppercase

# note:  i created this function to generate a tabula recta, but i realised this was not necessary with the main method i used, however i left this in as i like the approach i used to solve this problem
def tabulaRecta():
    import string
    alpha = list(string.ascii_uppercase)
    l2d = []
    #starts from the last letter and goes backwards to the first item
    for i in range(0,len(alpha),1):
        #picks an index and cuts this index from the index to the end, and adds everything before the index to the end
        l2d.append(alpha[i:] + alpha[:i])
    return l2d

def vCipher(plaintext, key):
    i = 0
    #remake key length to fit plaintext
    while len(key) != len(plaintext):
        if len(key) > len(plaintext):
            key = key[:len(plaintext)]
        elif len(key) < len(plaintext):
            key += key[:len(plaintext) - len(key)]
    #intialise a ciphertext string to the empty string
    cphtext = ""
    plaintext = plaintext.upper()
    key = key.upper()
    #For every letter in the plaintext
    for ch in plaintext:
        #convert the letter into ascii
        asciiNum = ord(ch)
        #if the char is not a letter, then do nothing
        if ch not in alpha:
            pass
        else:
            #add the shift value
            asciiNum += ord(key[i])
            i += 1
            #if the number is now beyond the alphabet (beyond or 90 (ASCII)) then mod by 26 to find the letter and add it to 65
            while asciiNum > 90:
                asciiNum = 65 + asciiNum % 26
        #convert the number back into a character and add it to the cipherttext
        cphtext += chr(asciiNum)
    return cphtext