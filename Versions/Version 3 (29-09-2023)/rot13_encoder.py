import codecs, os

os.system('cls')
os.system('cls')

os.system('cls')

os.system('cls')


def start():
    to_be_decoded = input("Enter what you wanted to be decoded from rot13: ")
    print(codecs.encode(to_be_decoded, 'rot13'))
    start()

start()