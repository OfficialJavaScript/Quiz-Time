import codecs, os

os.system('cls')

def start():
    to_be_decoded = input("Enter what you wanted to be encoded to base64: ")
    encode_me_bytes = to_be_decoded.encode('utf-8')
    encoded = codecs.encode(encode_me_bytes, 'base64')
    print(encoded.decode('utf-8'))
    start()

start()