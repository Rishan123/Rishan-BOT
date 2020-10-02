import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import PIL.Image as Image
from picamera import PiCamera

camera = PiCamera()
classifier_model ="https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
IMAGE_SHAPE = (224, 224)

classifier = tf.keras.Sequential([
    hub.KerasLayer(classifier_model, input_shape=IMAGE_SHAPE+(3,))
])

camera.capture('image.jpg')
sample_img = 'image.jpg'
sample_img = Image.open(sample_img).resize(IMAGE_SHAPE)
sample_img = np.array(sample_img)/255.0

result = classifier.predict(sample_img[np.newaxis, ...])
predicted_class = np.argmax(result[0], axis=-1)

labels_path = tf.keras.utils.get_file('ImageNetLabels.txt','https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
imagenet_labels = np.array(open(labels_path).read().splitlines())

predicted_class_name = imagenet_labels[predicted_class]
print("Prediction: " + predicted_class_name.title())
