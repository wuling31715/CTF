import sys, csv

def get_code():
    morse_list = list()
    with open('morse_code.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            morse_list.append(row)
    return morse_list

def encode(plaintext, morse_list):
    plaintext = plaintext.upper()
    cyphertext = str()
    for char in plaintext:
        for code in morse_list:
            if char == code[0]:
                cyphertext += code[-1]
                cyphertext += ' '
    return cyphertext[:-1]

def decrypt(cyphertext, morse_list):
    cypher_list = cyphertext.split()
    plaintext = str()
    for char in cypher_list:
        for code in morse_list:
            if char == code[-1]:
                plaintext += code[0]
    return plaintext
    
def main():
    morse_list = get_code()
    plaintext = input('plaintext:')
    cyphertext = encode(plaintext, morse_list)
    plaintext = decrypt(cyphertext, morse_list)
    print('cyphertext: %s' % cyphertext)
    print("plaintext: %s" % plaintext)

if __name__ == '__main__':
    main()