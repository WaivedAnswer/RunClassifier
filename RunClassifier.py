# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:04:31 2019

@author: quinn.ramsay
"""

from imageai.Prediction import ImagePrediction

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("resnet50_weights_tf_dim_ordering_tf_kernels.h5")
print (prediction.modelPath)
prediction.loadModel()


predictions, percentage_probabilities = prediction.predictImage("runner.jpg", result_count=5)
for index in range(len(predictions)):
    print(predictions[index] , " : " , percentage_probabilities[index])