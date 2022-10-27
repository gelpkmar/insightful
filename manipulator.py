import random
from pixelsort import pixelsort
from PIL import Image

class Manipulator:
    """ Manipulates an image according to data passed in as arguments """
    def __init__(self, hex_list):
        self.hex_list = hex_list

    def manipulate_hex_list(self, b_data, int_data):
        """ manipulate_hex_list takes a user_input (must be a string) and manipulates a given hex_list by randomly 
        chosing a starting point in the hexcode of the file and changing the next number of fields according to user_input
        (e.g. if user_input is 51, it will pick a random starting point and overwrite the next 51 fields with 51). """
        
        for i in range(int_data):
            random_start = random.randint(0, len(self.hex_list))
            if not random_start + (int_data*2) >= len(self.hex_list):
                self.hex_list[random_start] = b_data[0]
                self.hex_list[random_start+1] = b_data[1]
            else:
                print("Something went wrong, please try again.")
        return self.hex_list

    def sort_pixels(self, new_filename, user_input, avg_data, i):
        avg = avg_data
        i += 63
        # for i in range(30):
        #     a = Image.open(new_filename)
        #     avg += i*10
        #     b = pixelsort(a, angle=90, clength=avg)
        #     c = pixelsort(b, clength=avg)
        #     c.save(f"generated_files/gif/the_new{i}.png")
        a = Image.open(new_filename)
        b = pixelsort(a, angle=90, clength=avg)
        c = pixelsort(b, clength=avg)
        c.save(f"generated_files/{user_input}_altered.png")
        print(f"Finished! You can see your image at generated_files/{user_input}_altered.png")