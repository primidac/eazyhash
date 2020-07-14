# hash any string and get it copied directly to your clipboard

# importing all modules required for the program to run
from colorama import Fore, Style
from tqdm import tqdm
from time import sleep
from hashlib import *
import os
import pyperclip
import pyfiglet

# main program begins here
header =  Fore.GREEN + pyfiglet.figlet_format('EzHash', font='roman')
print(header)
print(Style.RESET_ALL)
print("...Ezhash values")


# command list
print('*' * 20)
print(' [*]Hash\n', 
      '[*]Version\n',
      '[*]Exit'
      )
print('*' * 20)

command = ['Hash', 'version', 'exit']
hash_algo = {'shake_128': shake_128, 'sha3_256': sha3_256, 'shake_256': shake_256, 'sha256': sha256, 'md5': md5, 'blake2s': blake2s, 'blake2b': blake2b, 'sha3_384': sha3_384, 'sha512' : sha512, 'sha3_224': sha3_224, 'sha224': sha224, 'sha3_512':sha3_512, 'sha384': sha384, 'sha1': sha1}
# prompt
while True:
    try:
        prompt = input('=>')
        if prompt == command[0]:
        	myhash = input('Hash Algo:')
        	string = input('String:')
        	if myhash in hash_algo.keys():
        		hashed = hash_algo[myhash](string.encode()).hexdigest()
        		print(Fore.GREEN)
        		for x in tqdm(range(int(100)), ascii=True, desc='Hashing'):
        			sleep(0.01)
        		pyperclip.copy(hashed)
        		print('hash copy to clipboard')
        		print(Style.RESET_ALL)
        	else:
        		print("Algorithm do not exist or not supported yet")
        		

    except Exception as e:
    	raise e

