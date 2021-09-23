
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


def encrypt(direction,text,shift):

    shift = shift % 25

    if(direction == 'encode' or direction =='decode'):
            
        text = text.lower()
        space_index = text.find(" ")
        # print(space_index)

        #find number of spaces

        b_space_list = list(text)
        a_space_list = []
        pos = 0
        for pos in range(0,len(b_space_list)):
            if b_space_list[pos] == " ":
                a_space_list.append(pos)
            
        # print(type(a_space_list))
        # print(a_space_list)

        x =text.replace(" ","")
        # print(f"text without space --> {x}")
        new_text_list = []
        text_list = list(x)
        # print(text_list)
        
        




        len_alpha = len(alphabet)
        for i in range (0, len(text_list)):
            alpha = text_list[i]
            curr_index = alphabet.index(alpha)
            new_index = curr_index + shift

                
            if new_index < len_alpha:
                new_alpha = alphabet[new_index]
            else:
                index_diff = new_index - len_alpha
                new_index = index_diff
                new_alpha = alphabet[new_index]
                

            # print(f"old alpha-->{alpha} and new alpha -->{new_alpha}")
            new_text_list.append(new_alpha)
            # except ValueError:
            #     space_index = i

        #Steps to inculdes spaces back

        for char in a_space_list:
            new_text_list.insert(char," ") 
            

        # print(f"new list --> {new_text_list}")

        # new_text_list.insert(space_index,' ')
        # print(f"new list --> {new_text_list}")
        print(f"encoded value is --> {''.join(new_text_list)} \nOriginal value is --> {text}")
        encoded_value = ''.join(new_text_list)
        decoded_value = text
        # print(encoded_value)
        
    
        
        
def decrypt(direction,text,shift):
    if(direction == 'encode' or direction =='decode'):
            
        text = text.lower()
        space_index = text.find(" ")
        # print(space_index)

        #find number of spaces

        b_space_list = list(text)
        a_space_list = []
        pos = 0
        for pos in range(0,len(b_space_list)):
            if b_space_list[pos] == " ":
                a_space_list.append(pos)
            
        # print(type(a_space_list))
        # print(a_space_list)

        x =text.replace(" ","")
        # print(f"text without space --> {x}")
        new_text_list = []
        text_list = list(x)
        # print(text_list)
        
        len_alpha = len(alphabet)
        for i in range (0, len(text_list)):
            alpha = text_list[i]
            curr_index = alphabet.index(alpha)
            new_index = curr_index - shift

                
            if new_index < len_alpha:
                new_alpha = alphabet[new_index]
            else:
                index_diff = new_index - len_alpha
                new_index = index_diff
                new_alpha = alphabet[new_index]
                

            # print(f"old alpha-->{alpha} and new alpha -->{new_alpha}")
            new_text_list.append(new_alpha)
            # except ValueError:
            #     space_index = i

        #Steps to inculdes spaces back

        for char in a_space_list:
            new_text_list.insert(char," ") 
            

        # print(f"new list --> {new_text_list}")

        # new_text_list.insert(space_index,' ')
        # print(f"new list --> {new_text_list}")
        print(f"decoded value is --> {''.join(new_text_list)} \nOriginal value is --> {text}")
        encoded_value = ''.join(new_text_list)
        decoded_value = text
        
        # print(decoded_value) 
        
        

# encrypt(direction = direction, text = text, shift = shift)

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