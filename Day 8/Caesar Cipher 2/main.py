alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def encrypt(original_text, shift_amount):
    effective_shift = shift % 26
    shift_part = alphabet[:effective_shift]
    shifted_alphabet = alphabet[effective_shift:] + shift_part
    print(shifted_alphabet)
    encoded_message = ""
    for letter in text:
        encoded_message += shifted_alphabet[alphabet.index(letter)]
    print(encoded_message)



def decrypt(original_text, shift_amount):
    effective_shift = shift % 26
    shift_part = alphabet[:effective_shift]
    shifted_alphabet = alphabet[effective_shift:] + shift_part
    print(shifted_alphabet)
    decrepted_message = ""
    for letter in text:
        decrepted_message += alphabet[shifted_alphabet.index(letter)]
    print(decrepted_message)

def caesar(encode_or_decode, original_text, shift_amount):
    if direction == 'encode':
        encrypt(original_text=text, shift_amount=shift)
    if direction == 'decode':
        decrypt(original_text=text, shift_amount=shift)


caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)
