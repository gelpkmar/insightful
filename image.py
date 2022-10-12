import binascii

class Image:
    """Models a digital image"""
    def __init__(self, path):
        self.path = path
        """ open_file opens a file in read mode and interprets it in binary.
        As argument it takes the filename of an existing file. """
        with open(self.path, "rb") as f:
            # memory-map the file, size 0 means whole file
            self.mm = f.read()
        
    def create_hex_list(self):
        #convert binascii to hex
        # hex = binascii.b2a_hex(self.mm)
        hex = binascii.hexlify(self.mm)
        #convert binary-hex to hex-list
        return list(hex)

    def save_image(self, new_filename, new_hex):
        """ 'hex' takes in the manipulated hex-binary and converts it to binascii the saves as 'new_file_name'.
        Generated files are stored in 'generated_files/' """
        with open("generated_files/"+new_filename, "w+b") as new_jpg:
            #convert hex-binary to binascii
            bin = binascii.unhexlify(new_hex)
            new_jpg.write(bin)

            #close the file
            return new_jpg.close()