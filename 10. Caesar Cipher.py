alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

want_to_continue = True
while want_to_continue:

    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt: \n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: \n"))

    def encrypt(edit_text,shift_ammount):
        cipher_text = ""
        for letter in edit_text:
            if letter in alphabet:

                position = alphabet.index(letter)
                new_position = position + shift_ammount
                if new_position >= 26:
                    new_position = new_position - 26
                else:
                    new_position
                new_letter = alphabet[new_position]
            else:
                new_letter = letter


            cipher_text += new_letter
        print(f"the encoded text is {cipher_text}")



    def decrypt(edit_text, shift_ammount):
        plain_text = ""
        for letter in edit_text:
            if letter in alphabet:
                position = alphabet.index(letter)

                if position < shift_ammount:
                    new_position = position - shift_ammount +1
                else:
                    new_position = position - shift_ammount
                new_letter = alphabet[new_position]

            else:
                new_letter = letter

            plain_text += new_letter
        print(f" the decoded text is {plain_text}")


    def cypher(cypher_direction):
        if cypher_direction == 'encode':
            encrypt(edit_text=text, shift_ammount=shift)
        elif cypher_direction == 'decode':
            decrypt(edit_text=text, shift_ammount=shift)
        else:
            print("Plese provide correct input")

    cypher(cypher_direction= direction)
    result = input('If you want to continue press yes else no: \n ')
    if result == 'yes':
        want_to_continue = True
    else:
        want_to_continue = False
