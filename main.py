import art
from image import Image
from manipulator import Manipulator

#constant which defines the original file to be edited.
# ORIGINAL_FILE = "../altered/altered_home_min.jpg"
ORIGINAL_FILE = "original_files/Mongolian_Steppe_original_min.jpg"
AMOUNT_OF_IMAGES = 1 # Change this value to change the number of individual images to be created.

# image = Image(ORIGINAL_FILE)

# current_hex_list = image.create_hex_list()

user_input = str(input("What do you want the new file be called? Please provide the absolute path ('.jpg' will be added at the end): "))
new_filename = str(user_input+".jpg")
temperature = str(input("What was the temperatur that day? Please provide in degrees Celsius: "))
int_temperature = int(temperature)
b_temperature_list = list(bytes(temperature.encode()))
humidity = str(input("What was the humidity that day? please provide in %: "))
int_humidity = int(humidity)
b_humidity_list = list(bytes(humidity.encode()))
air_pressure = str(input("What was the air pressure that day? Please provide in psi: "))
int_air_pressure = int(air_pressure)
b_air_pressure_list = list(bytes(humidity.encode()))

# manipulator = Manipulator(current_hex_list)

for i in range(AMOUNT_OF_IMAGES):
    image = Image(ORIGINAL_FILE)
    current_hex_list = image.create_hex_list()
    manipulator = Manipulator(current_hex_list)

    current_hex_list = manipulator.manipulate_hex_list(b_temperature_list, int_temperature)
    current_hex_list = manipulator.manipulate_hex_list(b_humidity_list, int_humidity)
    current_hex_list = manipulator.manipulate_hex_list(b_air_pressure_list, int_air_pressure)


    #converts hex-list back to hex-binarytemp
    new_hex = bytes(current_hex_list)

    #create a new file with the manipulated hex-binary
    image.save_image(new_filename, new_hex)

    avg_data = int((int_air_pressure+int_humidity+int_temperature)/3)

    manipulator.sort_pixels(str("generated_files/"+new_filename), user_input, avg_data, i)


