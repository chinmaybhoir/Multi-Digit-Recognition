# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:07:52 2017

@author: Chinmay.Bhoir
"""

import cv2
import numpy as np

def get_horizontal_projection(img):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    if img.shape[0] > 500 and img.shape[1] > 500:
        img = cv2.resize(img, ((500,500)))
    max_arr = np.sum(img, axis = 1)
    div1 = int(max_arr.shape[0] * (1/3))
    div2 = int(max_arr.shape[0] * (2/3))
    div3 = int(max_arr.shape[0] - 1)
    max_val1 = np.amax(max_arr[0:div1], axis=0)
    max_val2 = np.amax(max_arr[div1:div2], axis=0)
    max_val3 = np.amax(max_arr[div2:div3], axis=0)
    print("HR:: 1-",div1,"\t2-",div2,"\t3-",div3)
    breakpoints = np.zeros((1,max_arr.shape[0]), dtype = int)
    k = 0
    for i in range(0,max_arr.shape[0]):
        if i is 0:
            breakpoints[0][k] = 0
            k = k+1
            boundary_1 = -99
            boundary_2 = -99
        else:
            if i <= div1:
                if max_arr[i-1] < max_val1 and max_arr[i] == max_val1:
                    boundary_1 = i
                if max_arr[i-1] == max_val1 and max_arr[i] < max_val1:
                    boundary_2 = i
                if ((boundary_1 != -99) and (boundary_2 != -99) and (boundary_2 > boundary_1)):
                    boundary = int((boundary_1 + boundary_2) / 2)
                    breakpoints[0][k] = boundary
                    k = k+1
                    boundary_1 = -99
                    boundary_2 = -99
            if i <= div2 and i > div1:
                if max_arr[i-1] < max_val2 and max_arr[i] == max_val2:
                    boundary_1 = i
                if max_arr[i-1] == max_val2 and max_arr[i] < max_val2:
                    boundary_2 = i
                if ((boundary_1 != -99) and (boundary_2 != -99) and (boundary_2 > boundary_1)):
                    boundary = int((boundary_1 + boundary_2) / 2)
                    breakpoints[0][k] = boundary
                    k = k+1
                    boundary_1 = -99
                    boundary_2 = -99
            if i <= div3 and i > div2:
                if max_arr[i-1] < max_val3 and max_arr[i] == max_val3:
                    boundary_1 = i
                if max_arr[i-1] == max_val3 and max_arr[i] < max_val3:
                    boundary_2 = i
                if ((boundary_1 != -99) and (boundary_2 != -99) and (boundary_2 > boundary_1)):
                    boundary = int((boundary_1 + boundary_2) / 2)
                    breakpoints[0][k] = boundary
                    k = k+1
                    boundary_1 = -99
                    boundary_2 = -99
    breakpoints[0][k] = max_arr[(max_arr.shape[0])-1]
    images_list = []
    for i in range(0,k):
        images_list.append(img[breakpoints[0][i]:breakpoints[0][i+1],:])
    return images_list

def get_vertical_projection(img):
    max_arr = np.sum(img, axis = 0)
    div1 = int(max_arr.shape[0] * (1/3))
    div2 = int(max_arr.shape[0] * (2/3))
    div3 = int(max_arr.shape[0] - 1)
    max_val1 = np.amax(max_arr[0:div1], axis=0)
    max_val2 = np.amax(max_arr[div1:div2], axis=0)
    max_val3 = np.amax(max_arr[div2:div3], axis=0)
    print("VR:: 1-",div1,"\t2-",div2,"\t3-",div3)
    breakpoints = np.zeros((1,max_arr.shape[0]), dtype = int)
    k = 0
    for i in range(0,max_arr.shape[0]):
        if i is 0:
            breakpoints[0][k] = 0
            k = k+1
            boundary_1 = -99
            boundary_2 = -99
        else:
            if i <= div1:
                if max_arr[i-1] < max_val1 and max_arr[i] == max_val1:
                    boundary_1 = i
                if max_arr[i-1] == max_val1 and max_arr[i] < max_val1:
                    boundary_2 = i
                if ((boundary_1 != -99) and (boundary_2 != -99) and (boundary_2 > boundary_1)):
                    boundary = int((boundary_1 + boundary_2) / 2)
                    breakpoints[0][k] = boundary
                    k = k+1
                    boundary_1 = -99
                    boundary_2 = -99
            if i <= div2 and i > div1:
                if max_arr[i-1] < max_val2 and max_arr[i] == max_val2:
                    boundary_1 = i
                if max_arr[i-1] == max_val2 and max_arr[i] < max_val2:
                    boundary_2 = i
                if ((boundary_1 != -99) and (boundary_2 != -99) and (boundary_2 > boundary_1)):
                    boundary = int((boundary_1 + boundary_2) / 2)
                    breakpoints[0][k] = boundary
                    k = k+1
                    boundary_1 = -99
                    boundary_2 = -99
            if i <= div3 and i > div2:
                if max_arr[i-1] < max_val3 and max_arr[i] == max_val3:
                    boundary_1 = i
                if max_arr[i-1] == max_val3 and max_arr[i] < max_val3:
                    boundary_2 = i
                if ((boundary_1 != -99) and (boundary_2 != -99) and (boundary_2 > boundary_1)):
                    boundary = int((boundary_1 + boundary_2) / 2)
                    breakpoints[0][k] = boundary
                    k = k+1
                    boundary_1 = -99
                    boundary_2 = -99
    breakpoints[0][k] = max_arr[(max_arr.shape[0])-1]
    images_list = []
    for i in range(0,k):
        images_list.append(img[:,breakpoints[0][i]:breakpoints[0][i+1]])
    return images_list

img = cv2.imread("Keras_Theano/images/multi_digits2.png")

def get_images_list(img):
    horizontal_images_list = []
    horizontal_images_list = get_horizontal_projection(img)
    for i in range(0,len(horizontal_images_list)):
        if i is 0:
            images_list = []
        images_list.append(get_vertical_projection(horizontal_images_list[i]))
    images = []
    for i in range(0,len(images_list)):
        for j in range(0,len(images_list[i])):
            images.append(images_list[i][j])
    return images