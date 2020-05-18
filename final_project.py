"""
Author: Gerald Addo-Tetteh
CP4E Final Project.
The Program peforms encrpytions and the coresponding decryptions on a piece of text.
It program contains six different encryption methods with the corresponding decryptions.
"""

#Imported modules
import random
import sys
from turtle_keys import turtle_table


#This function creats a key that would be used for the encryptions below
def key_gen():
    key = ""
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?&,.'"
    for i in range(len(alpha)):
        index = random.randint(0,67-i)#A letter is selected at random and added to the key string
        letter = alpha[index]
        alpha = alpha.replace(letter,"")#To avoid duplicates each letter in key is removed from alpha
        key += letter
    return key


#This function creats a numeric key for image encryption
def key_numgen():
    numbers = [1,2,3,4,5,6,7,8,9]
    new_number = []
    #picks a random number from numbers and appends to new_number
    for x in range(len(numbers)):
        index = random.randint(0,8-x)#selects random number
        new_number.append(numbers[index])#number from numbers
        numbers.remove(numbers[index])#removes number from numbers to avoid repetition
    return new_number


"""
These functions are meant to avoid errors in the program .
If the user times in a file which can not be found the
program alerts the user.
"""


def enter_file(file_open):
     try:
         text = file_open
         file = open(text,"r")
         return file
     except FileNotFoundError:
         sys.stdout.write(""+"\n")
         sys.stdout.write("The file can not be found."+"\n")
         sys.stdout.write(""+"\n")
         return None

def test_image(file_open):
    try:
        text = file_open
        file = open(text,"rb")
        return file
    except FileNotFoundError:
         sys.stdout.write(""+"\n")
         sys.stdout.write("The file can not be found."+"\n")
         sys.stdout.write(""+"\n")
         return None



"""
This function is meant to avoid errors in the program.
If the user enters a values which is not in range
it alerts the user of the error.
"""



def enter_ans(num):
         try:
              number = num
              return number
         except ValueError:
             sys.stdout.write(""+"\n")
             sys.stdout.write("Your input is invalid"+"\n")
             sys.stdout.write(""+"\n")
         return None



# The dictionary contains all 26 letters and numbers with the corresponding encryption.
special_key = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
                        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
                        'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
                        'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
                        'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab',
                        'a':'00000', 'b':'00001', 'c':'00010', 'd':'00011', 'e':'00100',
                        'f':'00101', 'g':'00110', 'h':'00111', 'i':'01000', 'j':'01001',
                        'k':'01010', 'l':'01011', 'm':'01100', 'n':'01101', 'o':'01110',
                        'p':'01111', 'q':'10000', 'r':'10001', 's':'10010', 't':'10011',
                        'u':'10100', 'v':'10101', 'w':'10110', 'x':'10111', 'y':'11000', 'z':'11001',
                        '1':'12345', '2':'67890', '3':'10293', '4':'48576', '5':'11111',
                        '6':'22222', '7':'33333', '8':'44444', '9':'55555', '0':'66666', "?":"zxcvb",
                        "!":"23456"," ":'*s_*6'}
alpha_num  = key_gen()#random string
atbash_dictionary = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}


"""
The function below contains all the encryptions
available in the program.
"""


def encryption(encry_type,text):
        ans_array = []
        encryption_type = enter_ans(encry_type)#The user indicates the encryption needed.
        encrypted_text = ""




        #The code below performs the Ceasar cipher
        if encryption_type == 1:
            shifts = 5
            sys.stdout.write(""+"\n")
            plain_text = text
            plain_text = plain_text.replace(" ","")#Removes all spaces in plain_text

            """
            An iteration is performed over each item in plain_text to find its index.
            The index is increased by five and the returns the coresponding letter.
            """

            for ch in plain_text:
                idx = alpha_num.find(ch)
                new_index = (idx + shifts)%len(alpha_num)
                encrypted_text = encrypted_text + alpha_num[new_index]
            sys.stdout.write(""+"\n")
            sys.stdout.write("Each chracter in text was shifted five places using this string:\n" + alpha_num+"\n")
            sys.stdout.write(""+"\n")
            ans_array.append("Encrypted text is : " +encrypted_text)
            return ans_array





        #The code below performs the Baconian cipher
        elif encryption_type == 2:
            sys.stdout.write(""+"\n")
            plain_text = text

            """
            An iteration is performed over each item in plain_text
            and the coresponding value of the character in the dictionary(special_key)
            is returned.
            """

            for ch in plain_text:
                if ch in special_key:
                    encrypted_text += special_key[ch]
            sys.stdout.write(""+"\n")
            sys.stdout.write("You text was encrypted using this dictionary:\n" + str(special_key)+"\n")
            sys.stdout.write(""+"\n")
            ans_array.append("Encrypted text is : " +encrypted_text)
            return ans_array





        #The code below performs the Atbash cipher
        elif encryption_type == 3:
            sys.stdout.write(""+"\n")
            plain_text = text
            plain_text = plain_text.replace(" ","")#Removes all spaces in plain_text
            plain_text = plain_text.upper()#Coverts all charcters in plain_text to upper case

            """
            An iteration is performed over each item in plain_text
            and the coresponding value of the character in the dictionary(atbash_dictionary)
            is returned.
            """

            for ch in plain_text:
                if ch in atbash_dictionary:
                    encrypted_text += atbash_dictionary[ch]
                else:
                    encrypted_text += ch
            sys.stdout.write(""+"\n")
            sys.stdout.write("You text was encrypted using this dictionary:\n" + str(atbash_dictionary)+"\n")
            sys.stdout.write(""+"\n")
            ans_array.append("Encrypted text is : " +encrypted_text)
            return ans_array




        #The code below performs the ROT 47 cipher
        elif encryption_type == 4:
            shifts = 47
            sys.stdout.write(""+"\n")
            plain_text = text
            plain_text = plain_text.replace(" ","")#Removes all spaces in plain_text

            """
            An iteration is performed over each item in plain_text to find its index.
            The index is increased by forty-seven and the returns the coresponding letter.
            """

            for ch in plain_text:
                idx = alpha_num.find(ch)
                new_index = (idx + shifts)%len(alpha_num)
                encrypted_text = encrypted_text + alpha_num[new_index]
            sys.stdout.write(""+"\n")
            sys.stdout.write("Each chracter in text was shifted forty-seven places using this string:\n" + alpha_num+"\n")
            sys.stdout.write(""+"\n")
            ans_array.append("Encrypted text is : " +encrypted_text)
            return ans_array






        #The code below Encyptes an entire text file using Baconian cipher
        elif encryption_type == 5:
            file_ = enter_file(text)
            s = text.replace(".txt","")
            if file_ == None:
                ans_array.append("Check your input")
                return ans_array
            encrypted_file = open(s+"_encrypted.txt","w+")

            """
            An iteration is performed over each item in plain_text
            and the coresponding value of the character in the dictionary(special_key)
            is returned and saved in encrypted_text.
            """


            for ch in file_:
                for i in ch:
                    if i in special_key:
                        encrypted_file.write(special_key[i])
            encrypted_file.close()
            file_.close()
            sys.stdout.write(""+"\n")
            sys.stdout.write("You text was encrypted using this dictionary:\n" + str(special_key)+"\n")
            ans_array.append("Your encrypted text is saved with the same name as you input file but with the attachment '_encrypted'")
            return ans_array



        #The code below Encryptes an image_file
        elif encryption_type == 6:
            image_file = test_image(text)
            if image_file == None:
                ans_array.append("Check your input")
                return ans_array
            file_type = text.split(".")[1]
            encry_image = open("new_image."+file_type,"wb")
            image = image_file.read()#reads all of image file
            key = key_numgen()#generates random numerical key
            image = bytearray(image)
            i = 1
            #iterating over image binary and encryping Each
            for index, value in enumerate(image):
                image[index] = value^key[(i % len(key))]
                i += 1
            encry_image.write(image)
            encry_image.close()
            image_file.close()
            sys.stdout.write("They key used for encryption was: "+str(key)+"\n")
            ans_array.append("Your Encrypted image is saved as" + " "+ "new_image."+file_type )
            return ans_array







        else:
            sys.stdout.write("ERROR: Number not in range"+"\n")
            sys.stdout.write("Please check your input"+"\n")


"""
This function contains all the decryptions available
in the program.
"""


def decryption(array):
        decry_type = array[1]
        text = array[2]
        if len(array) == 4:
            key = array[3]
        ans_array = []
        decryption_type = int(enter_ans(decry_type))
        decrypted_text = ""





        #Perfroms the decryption for the the Ceasar cipher
        if decryption_type == 1:
            shifts = 5
            encrypted_text = text
            alpha_num = key
            encrypted_text = encrypted_text.replace(" ","")
            """
            Iterates through encrypted text and shifts
            each character five places backward using the key
            provided.
            """
            for ch in encrypted_text:
                idx = alpha_num.find(ch)
                new_index = (idx-shifts)%len(alpha_num)
                decrypted_text = decrypted_text + alpha_num[new_index]
            ans_array.append("Here is your decrypted text: " + decrypted_text)
            return ans_array






        #Performs the decryption for the Baconian cipher
        elif decryption_type == 2:
            encrypted_text = text
            encrypted_text = encrypted_text.replace(" ","")
            g = 0
            """
            The while continues until g is equal to the length of the encrypted text.
            The iteration is performed over every five values in the encrypted_text.
            """

            while True :
                if(g < len(encrypted_text)-4):
                    tem_string = encrypted_text[g:g + 5]
                    decrypted_text += list(special_key.keys())[list(special_key.values()).index(tem_string)]
                    g += 5
                else:
                    break
            ans_array.append("Here is your decrypted text: " + decrypted_text)
            return ans_array






        #Performs the decryption for the Atbash cipher
        elif decryption_type == 3:
            encrypted_text = text

            for ch in encrypted_text:
                if ch in atbash_dictionary:
                    decrypted_text += atbash_dictionary[ch]
                else:
                    decrypted_text += ch
            ans_array.append("Here is your decrypted text: " + decrypted_text)
            return ans_array




        #Performs the decryption for ROT 47
        elif decryption_type == 4:
            sys.stdout.write(""+"\n")
            shifts = 47
            encrypted_text = text
            sys.stdout.write(""+"\n")
            alpha_num = key
            encrypted_text = encrypted_text.replace(" ","")
            for ch in encrypted_text:
                idx = alpha_num.find(ch)
                new_index = (idx-shifts)%len(alpha_num)
                decrypted_text = decrypted_text + alpha_num[new_index]
            ans_array.append("Here is your decrypted text: " + decrypted_text)
            return ans_array




        #Performs the decryption on a text file
        elif decryption_type == 5:
            file1 = enter_file(text)
            f = text.replace("_encrpyted.txt","")
            if file1 == None:
                ans_array.append("Check your input")
                return ans_array
            decrypted_file = open(f+"_decrypted.txt","w+")
            file2 = file1.readlines()#All trhe text in file1 one is saved as a string in file2
            g = 0
            for ch in file2:
               while True :
                if(g < len(ch)-4):
                    tem_string = ch[g:g + 5]
                    decrypted_file.write(list(special_key.keys())[list(special_key.values()).index(tem_string)])
                    g += 5
                else:
                    break
            decrypted_file.close()
            file1.close()
            ans_array.append("Your Decrypted text is saved with the same name as the input file but with the extension '_decrypted'")
            return ans_array




        #Performs the decryption on an image
        elif decryption_type == 6:
            encry_image = test_image(text)
            if encry_image == None:
                ans_array.append("Check your input")
                return ans_array
            file_type = text.split(".")[1]
            decry_image = open("clear_image."+file_type,"wb")
            image = encry_image.read()#reads all lines in encry_image
            image = bytearray(image)
            i = 1
            #Iterates through image and resets the binary values
            for index, value in enumerate(image):
                image[index] = value^key[(i % len(key))]
                i += 1
            decry_image.write(image)
            decry_image.close()
            encry_image.close()
            return "Your Decrypted image is saved as"  + " "+ "clear_image."+file_type






        else:
            sys.stdout.write("ERROR: Number not in range"+"\n")
            sys.stdout.write("Please check your input"+"\n")




"""
This is the main function
that is the program.
"""

def gerald_encryption(array):
    if array == []:
        turtle_table()
        return "The array is empty"
    encry_de = enter_ans(array[0])
    ans = None

    # If the the encryption number(encry_de) is equal to 1 the following encryption methods can be performed.
    if encry_de == 1:
         ans = encryption(array[1],array[2])



    # If the the encryption number(encry_de) is equal to 2 the following encryption methods can be performed.
    elif encry_de == 2:
        ans = decryption(array)

    # If encry_de is out of range
    else:
        sys.stdout.write("ERROR: Number not in range"+"\n")
        sys.stdout.write("Please check your input"+"\n")
        turtle_table()
    # If ans is returned as a non type
    if ans == None:
        return "Check Values in array"
    else:
        return ans
