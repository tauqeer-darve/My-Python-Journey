#CAESER CIPHER
import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(original_text,shift_amount):
    output_text = ""
    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            index = alphabet.index(letter) + shift_amount
            index %= len(alphabet)
            output_text += alphabet[index]
    print(f"{direction}d message is: {output_text}")

flag = True
while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(original_text=text,shift_amount=shift)
    flow = input("Do you want to continue? Type 'yes' or 'no': ").lower()
    if flow == "no":
        print("Goodbye")
        flag = False