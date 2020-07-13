# hash any string easily with ezhash

# importing all modules required by the program
from hashlib import *
from colorama import Fore, Style
from tqdm import tqdm
import pyfiglet
import pyperclip


# hashing function
def ezhashed(value):
    hashed_algo = {'shake_128': shake_128, 'sha256': sha256, 'sha3_256': sha3_256, 'sha3_224': sha3_224, 'sha1': sha1, 'sha224': sha224, 'sha384': sha384 , 'sha512': sha512, 'sha3_384': sha3_384, 'blake2b': blake2b, 'blake2s': blake2s , 'shake_256': shake_256, 'sha3_512': sha3_512, 'md5': md5}
    name = 'primidac'
    if value in hashed_algo.keys():
        value(name.encode()).hexdigest()

# main program begins here
# making our parser
ez_parser = argparse.ArgumentParser(prog="ezhash",
    description="EzHash is a simple tool to hash any string from your command line and get it copied directly to your clipboard")

# making our command for our programs
ez_parser.add_argument(
    "-v",
    "--version",
    action='store_true',
    help='Displays the current version of EzHash you are running'
)

ez_parser.add_argument(
    "-hs",
    "--hash",
    "-ha",
    "--hash_algo",
    action='store_true',
    # type='int',
    help='Returns the hash of any value'
)

# creating our parser object
args = ez_parser.parse_args()

# bringing our program to life
if args.version:
    print('Running V1.0.4')


elif args:
    # program header
    header = pyfiglet.figlet_format('EzHash' , font='roman')
    print(Fore.GREEN + header)
    print(Style.RESET_ALL)
    os.system('python3 ezhash.py -h')
