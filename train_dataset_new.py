import cv2
import os
import numpy as np
import faceRecognition as fr
import urllib.request
import time
from win10toast import ToastNotifier 

def train_model():
    faces,faceID=fr.labels_for_training_data('training_images')
    face_recognizer=fr.train_classifier(faces,faceID)
    face_recognizer.save('trainingData.yml')
    return 2


	
