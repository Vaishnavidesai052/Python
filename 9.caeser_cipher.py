alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
shift = int(input("Type the shift number:\n"))
text = input("Type your message:\n").lower()

def caesar(original_text, shift_amount, cipher_direction):
    # Normalize shift in case user enters large number
    shift_amount %= len(alphabet)
    
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if cipher_direction == "encode":
                new_position = (position + shift_amount) % len(alphabet)
            elif cipher_direction == "decode":
                new_position = (position - shift_amount) % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter  # Keep non-alphabet characters as is
    
    print(f"Here is the {cipher_direction}d result: {cipher_text}")

# Call the single function
if direction in ["encode", "decode"]:
    caesar(original_text=text, shift_amount=shift, cipher_direction=direction)
else:
    print("Invalid input! Type 'encode' or 'decode'.")
