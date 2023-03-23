import argparse
import hashlib
import time
import pyfiglet

class BruteForce:



    def __init__(self):
        print("Brute force starting...\n")


    def show_figlet(self):

        result_ascii = pyfiglet.figlet_format("F4rceDestroyer{<")
        print(result_ascii)
        time.sleep(4)



    def get_hashAndwordlist_file(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-hf', '--hashfile', type=str, help="you must enter the hash file")
        parser.add_argument('-wf', '--wordlist', type=str, help="You must enter the wordlist file")
        args = parser.parse_args()

        if args.hashfile != None and args.wordlist != None:

            return args


        else:
            print("You must enter the hashfile and wordlist..")




    def hash_the_crack(self, hashfile, wordlist):

        with open(wordlist, 'r') as file:
            password_read = file.readlines()


        with open(hashfile, 'r') as file:
            hash_read = file.readline().strip()
            hash_read = hash_read.lower()


        for password in password_read:
            hashed_password = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()

            """
            We are trying to convert the passwords to hash sha256 format and 
            compare them with the actual hash and try to crack them.
            """

            if hashed_password == hash_read:

                print("HASH:{0}\n".format(hash_read))
                print("HASH CRACKCED!!")
                print("Crack Password:{0}".format(password))


                return

        print("Hash not found :(")





if __name__ == '__main__':

    start_time = time.time()

    bruteforce = BruteForce()
    bruteforce.show_figlet()
    args = bruteforce.get_hashAndwordlist_file()
    bruteforce.hash_the_crack(args.hashfile, args.wordlist)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"The passing time: {elapsed_time:.2f} seconds")
