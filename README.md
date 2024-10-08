# Technion ECE 046211

<h1 align="center">
  <br>
 Deep Learning Project -  
  Evyatar Cohen and Reut Cohen 
  <br>
  <img src="https://raw.githubusercontent.com/taldatech/ee046211-deep-learning/main/assets/dl_intro_anim.gif" height="200">
</h1>


# Handwritten Mathematical Expression Solver Using YOLO


<h1 align="center">
  <br>
  <img src="https://github.com/evyatar1322/Deep-learning-project/blob/main/images/detection.jpg" height="150">
  <br>
</h1>

## Project Overview
This project aims to develop a system capable of detecting and solving handwritten mathematical expressions using a YOLO (You Only Look Once) model. The primary objective is to train the YOLO model to accurately recognize digits and mathematical operators, process an image containing a handwritten equation, and then compute and display the solution.

## Features
- **Digit and Operator Detection:** Uses a YOLO model trained on images of handwritten digits (0-9) and mathematical operators (plus, minus, multiplication, division).
- **Equation Extraction:** Capable of extracting and interpreting expressions from images of handwritten text.
- **Solution Computation:** Solves the detected mathematical expression and displays the result.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/evyatar1322/Deep-learning-project

   
## Instructions for running the model
- **Upload dataset** - To train the model from scratch, you need to upload the folder "data3.zip" which contains folders of all the operators and digits,
So for example in "data3.zip/0" there are pictures of the number 0
- **Train the model from scratch** - The "Training.ipynb" contains the model training code.
- **Use trained model** - In the file "Calculating.ipynb" you can load the trained model and run it on an image of an equation of your choice.
- **Our trained model** - Inside "session_backup.zip\detect\train\weights" you can find our weights for the model
 

## ✨ Flow ✨

### 📂 First Step: Preparing the Dataset
The initial step involves processing the dataset by generating an 
annotation file for each image. This file contains the coordinates 
of the objects within the image and their corresponding class labels. 
This step is crucial for training the YOLO model, as it provides the 
necessary data for the model to learn the relationships between the 
images and the object classes they contain.
(class_id center_x center_y width height)
<h1 align="center">
  <td><img src="https://github.com/evyatar1322/Deep-learning-project/blob/main/images/05Yyjvq9.jpg" height="100"></td>
   <td><img src="https://github.com/evyatar1322/Deep-learning-project/blob/main/images/text05Yyjvq9.jpg" height="100"></td>
</h1>

### 🧩 Second Step: Creating Test Equations
In this stage, we use a custom script to generate test equations from 
images not used during training. This includes both programmatically 
generated equations from new data base and equations written by hand.
<h1 align="center">
  <img src="https://github.com/evyatar1322/Deep-learning-project/blob/main/images/equation2.png" height="70">
</h1>

### 🎓 Third Step: Training the Model
With the prepared dataset, we train the YOLOv10 model. The hyperparameters 
for training are selected experimentally, allowing for fine-tuning of the 
model to achieve optimal performance. This iterative process helps to 
enhance the model's accuracy in detecting and classifying handwritten 
digits and operators.

### 🧪 Fourth Step: Testing and Refining
Post-training, we test the model by feeding it images of equations from the validation set. 
The model processes these images, identifying and classifying the digits and operators.
<h1 align="center">
  <img src="https://github.com/evyatar1322/Deep-learning-project/blob/main/images/success_readme.jpg" height="150">

#### Repeat steps 3 and 4 to get the best results
</h1>

### 🎯 Fifth Step: Final Evaluation
Once satisfactory performance is achieved through training and validation, 
we evaluate the model on the test set. This final step involves calculating 
the model's accuracy and determining its effectiveness in solving handwritten 
mathematical expressions.
<h1 align="center">
  <img src="https://github.com/evyatar1322/Deep-learning-project/blob/main/images/detection1.jpg" height="150">
  </h1>
  <h1 align="center">
  <img src="https://github.com/evyatar1322/Deep-learning-project/blob/main/images/detection2.jpg" height="150">
  </h1>
  <h1 align="center">
  <img src="https://github.com/evyatar1322/Deep-learning-project/blob/main/images/miss_detection.jpg" height="150">
</h1>

<h1 align="center">
  <tr>
    <td><img src="https://github.com/evyatar1322/Deep-learning-project/blob/main/images/same_data_result.jpg" height="75"></td>
    <td><img src="https://github.com/evyatar1322/Deep-learning-project/blob/main/images/other_data_result.jpg" height="75"></td>
    <td><img src="https://github.com/evyatar1322/Deep-learning-project/blob/main/images/our_result.jpg" height="75"></td>
  </tr>
</h1>


### Libraries that are required for the model

|Library         |
|----------------|
|`numpy`| 
|`matplotlib`|
|`zipfile`|
|`os`|
|`random`| 
|`shutil`| 
|`cv2`| 
|`time`|
|`torch`|
|`from torchvision import datasets, transforms`|
|`from torch.utils.data import DataLoader, Dataset`| 
|`from PIL import Image`| 
|`from google.colab import drive`|

#### Note:
The running results of our model and the weights can be found in **"session_backup.zip"**

