"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    resu=''
    for letter in plain_text:
        old_pos=alphabet.index(letter)
        new_position = old_pos + shift_amount
        resu+=alphabet[new_position]
    print(f" the encoded text is = {resu}")

def decrypt (plain_text,shift_amount):
    resu=""
    for letter in plain_text:
        old_pos= alphabet.index(letter) #index(letter,26) works too 
        new_position= old_pos-shift_amount
        resu+= alphabet[new_position]
    print(f" the decrypted text is = {resu}")
   
if direction=="encode":
    encrypt(text,shift)
else:
    decrypt(text,shift)
=========================================================================================

def caeser(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
        shift_amount*= -1
    for letter in start_text:
        position= alphabet.index(letter)
        
        new_position=position+shift_amount
        end_text+=alphabet[new_position]
    print(f"the {start_text} text is = {end_text}")

caeser(start_text=text,shift_amount=shift,cipher_direction=direction)
"""

#import art
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
       position = alphabet.index(char)
       new_position = position + shift_amount
       end_text += alphabet[new_position]
    else:
      end_text+= char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")



#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 



#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

choice="yes"
while choice == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=45%26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  choice=input("would you like to try again yes/no")