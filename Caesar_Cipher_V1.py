
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
from caesar_art import logo

print(logo)

def encrypt(direction,text,shift):

    shift = shift % 25

    text = text.lower()
    
    cipher_text_list = []
    position = 0
    # ************************
    
    alphabet_len = len(alphabet)
    for char in list(text):
        if char in alphabet:
            position = alphabet.index(char)
            new_pos = position + shift
            
            if new_pos < alphabet_len:
                # new_pos = alphabet[new_index]
                cipher_text_list += alphabet[new_pos]
            else:
                index_diff = new_pos - alphabet_len
                new_pos = index_diff
                cipher_text_list += alphabet[new_pos]

        else:
            cipher_text_list += char


    encoded_string = ''.join(cipher_text_list)

    print(f"the decoded value is ---> {encoded_string}")
    
        
        
def decrypt(direction,text,shift):
    shift = shift % 25

    text = text.lower()
    alphabet_len = len(alphabet)
    decipher_text_list = []
    position = 0
    # ************************
    for char in list(text):
        if char in alphabet:
            position = alphabet.index(char)
            new_pos = position - shift

            if new_pos < alphabet_len:
                # new_pos = alphabet[new_index]
                decipher_text_list += alphabet[new_pos]
            else:
                index_diff = new_pos - alphabet_len
                new_pos = index_diff
                decipher_text_list += alphabet[new_pos]

        else:
            decipher_text_list += char

    decoded_string = ''.join(decipher_text_list)

    print(f"the decoded value is ---> {decoded_string}")
    
       
        
        



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
status = True
while status:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction =='encode':
        encrypt(direction = direction, text = text, shift = shift)
    else:
        decrypt(direction = direction, text = text, shift = shift)
    user_res = input("Do you want to continue? -- Yes Or No \n")
    if(user_res == 'Yes'):
        status = True
    else:
        status = False