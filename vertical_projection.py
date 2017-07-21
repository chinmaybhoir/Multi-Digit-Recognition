# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:56:22 2017

@author: Chinmay.Bhoir
"""

import numpy as np
import cv2
import pickle
#import matplotlib.pyplot as plt
# CALCULATE THE SUM OF EVERY COLUMN
img = cv2.imread("Keras_Theano/images/Letters.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
def get_vertical_projection(img):
    print("img shape:",img.shape)
    gray_arr = np.sum(img, axis = 0)
    print("in vertical_proj. gray_arr=",gray_arr)
    '''
    plt.subplot(221)
    plt.plot(gray_arr)
    plt.subplot(223)
    plt.imshow(gray_img)
    '''
    max_val = np.amax(gray_arr, axis=0)
    breakpoints = np.zeros((1,gray_arr.shape[0]))
    k = 0
    for i in range(0,gray_arr.shape[0]):
        if i is 0:
            breakpoints[0][k] = 0
            k = k+1
        else:
            if gray_arr[i-1] < max_val and gray_arr[i] == max_val:
                breakpoints[0][k] = i
                k = k+1
    breakpoints[0][k] = gray_arr[gray_arr.shape[0]-1]
    images_list = []
    for i in range(0,k):
        images_list.append(img[:,int(breakpoints[0][i]):int(breakpoints[0][i+1])])
    return images_list
images_list = get_vertical_projection(img)
images_list_file = pickle.dump(images_list,open("img_list.p", "wb"))