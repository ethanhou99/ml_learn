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

## Tagging method
1. The tagging method is from https://www.neurala.com/
2. Another tagging method is using labelImage.
3. Both of these two methods are shown as below:
<img src="https://github.com/ethanhou99/ml_learn/blob/master/images/tagging%20example.png" />
<img src="https://github.com/ethanhou99/ml_learn/blob/master/images/tagging%20exampleII.png" />
4. About 500 images are trained by both method.

## Training method
Two method are used to train the model:
   - Method1:https://www.youtube.com/playlist?list=PLQVvvaa0QuDcNK5GeCQnxYnSSaar2tpku
   - Method2:https://github.com/ethanhou99/ml_learn/blob/master/model2.ipynb (also in the main folder model2.ipynb)
   - Again, model1 can be dowloaded from https://drive.google.com/file/d/1U3SxjOcr4FsYsG2gd9nVJHsJ-w4sJR18/view and model2 is in the main folder directly called model2.h5
