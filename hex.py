import mmap
import binascii
import random

ORIGINAL_FILE = "Mongolian_Steppe_original.JPG"

def save_image(new_filename, hex):
    with open("generated_files/"+new_filename, "w+b") as new_jpg:
        bin = binascii.unhexlify(hex)
        new_jpg.write(bin)

        #close the file
        return new_jpg.close()

def open_file(filename):
    with open(filename, "rb") as f:
        # memory-map the file, size 0 means whole file
        mm = f.read()
    return mm

def manipulate_hex_list(user_input, hex_list):
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
    hex = binascii.b2a_hex(current_mm)
    hex_list = list(hex)
    
    hex_list = manipulate_hex_list(user_input=temp, hex_list=hex_list)
    hex_list = manipulate_hex_list(user_input=temp, hex_list=hex_list)
    hex_list = manipulate_hex_list(user_input=temp, hex_list=hex_list)


    hex = bytes(hex_list)
    return save_image(new_filename, hex)

#beginning of program

# current_file = str(input("Which Photo do you want to manipulate? Please provide absolute path: "))
temp = int(input("What was the temperatur that day? Please provide in degrees Celsius: "))
hum = str(input("What was the humidity that day? "))
air = str(input("What was the air pressure that day? "))

current_file_mm = open_file(ORIGINAL_FILE)

new_filename = str(input("What do you want the new file be called? Please provide the absolute path: "))

manipulate_image(new_filename=new_filename, current_mm=current_file_mm, temp=temp, humidity=hum, air_pressure=air)

