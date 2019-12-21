def encode(plaintext, public_key, n):
    cyphertext = (plaintext ** public_key) % n    
    return cyphertext

def decode(cyphertext, private_key, n):
    plaintext = (cyphertext ** private_key) % n
    return plaintext

def decode2(cyphertext, private_key_fact_list, n):
    for i in private_key_fact_list:
        cyphertext = (cyphertext ** i) % n
    plaintext = cyphertext
    return plaintext