# Machine Learning Project
This project can detect the vehicle type in an image and circle out the object position.
<img src="https://github.com/ethanhou99/ml_learn/blob/master/output_images/test2.jpg" />
<img src="https://github.com/ethanhou99/ml_learn/blob/master/output_images/test7.jpg" />

## Instruction
To use this API, please set up the enviroment as follow:
1. Create a new folder and run terminal under this folder's path
2. Type in the folloing code:
   ```
   git init
   git clone https://github.com/ethanhou99/ml_learn
   ```
3. Save the images you plan to test to the 'test_images'(must be .jpg files)
4. Since the model is too large, you need to download the model from: 
   https://drive.google.com/open?id=1U3SxjOcr4FsYsG2gd9nVJHsJ-w4sJR18
   Then, save it to the main folder you created.
5. Right now, your main folder should have four sub-folders: font, output_images, resource, test_images;
   and main.py, SSD300.hdf5(model)
6. Run the mian.py
7. The recognize result are saved in the output_images folder
