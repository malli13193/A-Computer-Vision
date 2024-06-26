First, walk through the executable Colab notebook.

Start by importing TensorFlow.


import tensorflow as tf
print(tf.__version__)
You'll train a neural network to recognize items of clothing from a common dataset called Fashion MNIST. It contains 70,000 items of clothing in 10 different categories. Each item of clothing is in a 28x28 grayscale image. You can see some examples here:



The labels associated with the dataset are:

Label

Description

0

T-shirt/top

1

Trouser

2

Pullover

3

Dress

4

Coat

5

Sandal

6

Shirt

7

Sneaker

8

Bag

9

Ankle boot

The Fashion MNIST data is available in the tf.keras.datasets API. Load it like this:


mnist = tf.keras.datasets.fashion_mnist
Calling load_data on that object gives you two sets of two lists: training values and testing values, which represent graphics that show clothing items and their labels.


(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
What do those values look like? Print a training image and a training label to see. You can experiment with different indices in the array.


import matplotlib.pyplot as plt
plt.imshow(training_images[0])
print(training_labels[0])
print(training_images[0])
The print of the data for item 0 looks like this:



You'll notice that all the values are integers between 0 and 255. When training a neural network, it's easier to treat all values as between 0 and 1, a process called normalization. Fortunately, Python provides an easy way to normalize a list like that without looping.


training_images  = training_images / 255.0
test_images = test_images / 255.0
You may also want to look at 42, a different boot than the one at index 0.

Now, you might be wondering why there are two datasets—training and testing.

The idea is to have one set of data for training and another set of data that the model hasn't yet encountered to see how well it can classify values. After all, when you're done, you'll want to use the model with data that it hadn't previously seen! Also, without separate testing data, you'll run the risk of the network only memorizing its training data without generalizing its knowledge.
