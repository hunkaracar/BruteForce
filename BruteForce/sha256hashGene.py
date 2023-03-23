import hashlib

def sha256_hash_generator(get_input):

    hash = hashlib.sha256(get_input.encode('utf-8')).hexdigest()

    return hash


hash_pass = input("Convert to hash>>>")
print(sha256_hash_generator(hash_pass))