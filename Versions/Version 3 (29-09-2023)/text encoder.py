import codecs, os, platform

types_of_codecs = "base64\nbase64_codec\nbase_64\nbz2\nbz2_codec\nhex\nhex_codec\nquopri\nquopri_codec\nquoted_printable\nquotedprintable\nrot_13\nuu\nuu_codec\nzip\nzlib\nzlib_codec"

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        os.system('clear')

def ask_encode():
    print(types_of_codecs)
    encoder_type = input("What do you want your text to be encoded in? ")
    start(encoder_type)

def encoder(encode_me, encoder_type):
    encode_me_bytes = encode_me.encode('utf-8')
    encoded_text = codecs.encode(encode_me_bytes, "'" + encoder_type + "'")
    print(encoded_text)
    start(encoder_type)

def start(encoder_type):
    encode_me = input("Enter the text you want to be encoded (change encoder enter -1): ")
    if encode_me == "-1":
        ask_encode()
    else:
        encoder(encode_me, encoder_type)
        

clear_screen()
ask_encode()