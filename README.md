# Latin-Alphabet-Recognition-Using-Convolutional-Neural-Networks-in-Tensorflow
Recognizes Images of Latin Alphabet with up to 89% accuracy. Credits to gregv for his dataset on Kaggle which can be found here: https://www.kaggle.com/gregvial/comnist

# Data Cleaning and Preprocessing
The dataset came in a folder with subdirectories corresponding to the labels of the images which it holds i.e. images/Latin/A held all the images of A, images/Latin/B held all the images of B, and so on. The file, data.py, walks over the dataset and prepares the data in two npy files named train.npy and train_labels.npy making sure that they are shuffled to maintain initial randomness. The train.npy file contains the images opened through PIL(Python Imaging Library) which were resized to 28x28 and grayscaled to save space and make computation easier/quicker. The train_labels.npy contains the labels corresponding to the letters each image represents. They are one hot encoded into row vectors where the position of each on bit depends on the position of the letter in the alphabet i.e. A -> [1,0,0,...], B ->[0,1,0,...], C -> [0,0,1,..], and so on. Data Cleaning and Preprocessing was done by the data.py file.

# Neural Network Design
The neural network took in 28x28 grayscaled images fed into tensorflow tensors with dimension [n, 28, 28, 1] holding number of images, width, height, and number of input channels respectively. It applies a convolution layer the image with a window of size 5x5 and having a stride of [1,1,1,1] which explains how the filter moves through the dimensions of the input. An activation of ELU is then applied. A max pooling layer then pools the contents of the image using max pooling over a 2x2 window with a stride of [1, 2, 2, 1]. The convolution and pulling are repeated once more. The output of convolutions and pooling are then flattened into a vector. It is fed into a final set of densely connected layers with 1024, 525, and 26 neurons respectively each with an ELU activation except for the final layer which has a softmax activation

# Training
The loss function I used was cross entropy loss optimized via the Adam Optimizer with a learning rate of 10^-4 using backpropagation. I ran one batch per iteration with a batch size of 64 and ran that for 150k iterations which totals to about 856 epochs. I had the program display the training accuracy at every 100th iteration. I used a Tesla K80 GPU Instance on Floydhub with the Jupyter Notebook  and tensorflow environment to train the model.

# Training Results
The final accuracy on the test came to about 89% on the test set with this setup. The training accuracy converged at 98% around the 120kth iteration. In my original setup I only had 2 fully connected layers with sizes 1024 and 26 using RELU activation at 50k iterations and I got 83% accuracy with this on the test set. I added this new layer in and my accuracy plummeted to 25%. This occurred due to the vanishing gradient which especially impacts deep neural networks. I then came across this paper https://arxiv.org/pdf/1511.07289.pdf and I changed my activations to ELU which significantly helped reduce the vanishing gradients effects. I needed to crank up the number of iterations because the gradients would decrease as they propagated through the network.

# Conclusion
I am pretty happy with results as this was the first Deep Neural Network I have written and trained. I have learned many things such as the tensorflow library, the machine learning workflow, debugging models, searching for solutions off the web, and creating GPU Instances for cloud computing. Using the knowledge and experience gained by this mini project, I will try other, more complex tasks in computer vision such as emotion detection with people. I will also explore many other types of Neural Networks such as Recurrent Neural Networks, General Adversarial Networks, and Sequence to Sequence Models.
