# ROT13 CIPHER for encrpt or decrpt the text

def rot13_transformation(text) :
    result=[] # list to store the transformed characters


# Iterate through each chr in input text
    for char in text :

        if 'a'<=char<='z' :
            offset=ord('a')  # getting ascii value of 'a' for refrence 
            # ROT 13 logic applying to list for lower case
            result.append(chr((ord(char)-offset+13)%26+offset))
        elif 'A'<=char<='Z' :
            offset=ord('A')  # getting ascii value of 'A' for refrence 
            # ROT 13 logic applying to list for upper case
            result.append(chr((ord(char)-offset+13)%26+offset)) 
        else:
            result.append(char)

    return ''.join(result) # returning the transformed text as a string


""" MAIN FUNCTION """
def main() :
    print("/-------- ROT13 Encoder/Decoder --------/")
    print("1. Encrypt")
    print("2. Decrypt")
    choice=input("Choose an option (1 or 2) : ")

    if choice not in ['1','2'] :
        print("Invalid choice. Exiting the program .....")
        return

    text=input("Enter text : ")
    result=rot13_transformation(text)
    action="Encrypted" if choice=='1' else "Decrypted"
    print(f"{action} text : {result}")

main()

# END
