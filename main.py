import mmap
import binascii
import random
import art

#constant which defines the original file to be edited.
ORIGINAL_FILE = "Mongolian_Steppe_original.JPG"

def save_image(new_filename, hex):
    """ 'hex' takes in the manipulated hex-binary and converts it to binascii the saves as 'new_file_name'.
    Generated files are stored in 'generated_files/' """
    with open("generated_files/"+new_filename, "w+b") as new_jpg:
        #convert hex-binary to binascii
        bin = binascii.unhexlify(hex)
        new_jpg.write(bin)

        #close the file
        return new_jpg.close()

def open_file(filename):
    """ open_file opens a file in read mode and interprets it in binary.
    As argument it takes the filename of an existing file. """
    with open(filename, "rb") as f:
        # memory-map the file, size 0 means whole file
        mm = f.read()
    return mm

def manipulate_hex_list(user_input, hex_list):
    """ manipulate_hex_list takes a user_input (must be a string) and manipulates a given hex_list by randomly 
    chosing a starting point in the hexcode of the file and changing the next number of fields according to user_input
    (e.g. if user_input is 51, it will pick a random starting point and overwrite the next 51 fields with 51). """
    for i in range(user_input):
        count = 0
        random_start = random.randint(0, len(hex_list))
        if not random_start + user_input >= len(hex_list):
            hex_list[random_start+count] = user_input
            count += 1
        elif not random_start + user_input <= len(hex_list):
            hex_list[random_start+count] = user_input
            count -= 1
    return hex_list

def manipulate_image(new_filename, current_mm, temp, humidity, air_pressure):
    """ manipulate_image takes in the 4 values requested by the user as well as the memory-map generated in open_file(),
    converts the mm to a list of hex-values and then triggers the manipulate_hex_list() function for each of the user_inputs """
    #convert binascii to hex
    hex = binascii.b2a_hex(current_mm)
    #convert binary-hex to hex-list
    hex_list = list(hex)
    
    #manipulate the image with each of the provided inputs
    hex_list = manipulate_hex_list(user_input=temp, hex_list=hex_list)
    hex_list = manipulate_hex_list(user_input=temp, hex_list=hex_list)
    hex_list = manipulate_hex_list(user_input=temp, hex_list=hex_list)

    #converts hex-list back to hex-binary
    hex = bytes(hex_list)
    #create a new file with the manipulated hex-binary
    return save_image(new_filename, hex)

#beginning of program

print(art.logo)
print("Welcome to insightful. Provide the data that was recorded during the capture of the photo and see how your image changes.\n")

# current_file = str(input("Which Photo do you want to manipulate? Please provide absolute path: "))
temp = int(input("What was the temperatur that day? Please provide in degrees Celsius: "))
hum = str(input("What was the humidity that day? "))
air = str(input("What was the air pressure that day? "))

current_file_mm = open_file(ORIGINAL_FILE)

new_filename = str(input("What do you want the new file be called? Please provide the absolute path: "))

manipulate_image(new_filename=new_filename, current_mm=current_file_mm, temp=temp, humidity=hum, air_pressure=air)

