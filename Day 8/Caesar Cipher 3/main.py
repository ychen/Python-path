import art
# TODO-1: Import and print the logo from art.py when the program starts.
print(art.logo)



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




def caesar(encode_or_decode, original, shift_amount):
    effective_shift = shift % 26
    shift_part = alphabet[:effective_shift]
    shifted_alphabet = alphabet[effective_shift:] + shift_part
    print(shifted_alphabet)
    message = ""
    for letter in original:
        if letter not in alphabet:
            message += letter
        if letter in alphabet:

            if encode_or_decode == 'encode':
                message += shifted_alphabet[alphabet.index(letter)]
            if encode_or_decode == 'decode':
                message += alphabet[shifted_alphabet.index(letter)]
    print(message)


caesar(encode_or_decode=direction, original=text, shift_amount=shift)
# TODO-2: What happens if the user enters a number/symbol/space?










# TODO-3: Can you figure out a way to restart the cipher program?
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(encode_or_decode=direction, original=text, shift_amount=shift)
    to_continue = input("Type 'yes' if you want to go again. Otherwise, type 'no'").lower()
    if to_continue == 'no':
        should_continue = False





