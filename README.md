# insightful

This is the script used to create the files displayed in the following post: 

## (Mis-) Using a camera as a sensor among many.

This is a prototype script used to alter images using atmospherical data recorded at the time of image capture.

At the time the image is taken, also a range of other data about the cameras environment is collected (currently only temperature in Celsius, air pressure in psi and air humidity in % delivered as written input). The algorithm then takes these data points and changes the bits of the image by pasting in the data collected at random locations in the image-file's underlying structure:
1. The image is converted to an array consisting of its hex-data.
2. In turn, temperature, air pressure and humidity is converted into hex and a number of positions in the hex array are replaced with this value (the number is equal to the number the value represents - e.g. if temperature is 16 degrees celcius, 16 is pasted as hex in 16 random places in the array)
3. After the hex code of the image was changed, a new .jpg file is created as an intermediate version.
4. The average value of the three above recorded values is calculated an used as input along with the intermediate image from step 3 for the Pixelsorting algorithm found here: https://github.com/satyarth/pixelsort.
5. A new .png image is created as the final product.

One could argue that the data collected is now a part of the image, the camera (mis) used as a sensor among others. Fused into one with the image, the data is visualized as what it is, an atmospherical sensation. I call them: "Insights".