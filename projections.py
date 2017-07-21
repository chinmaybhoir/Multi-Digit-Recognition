# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:09:41 2017

@author: Chinmay.Bhoir
"""


#from horizontal_projection import get_horizontal_projection

import cv2
import numpy as np

def get_horizontal_projection(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    if img.shape[0] > 500 and img.shape[1] > 500:
        gray_img = cv2.resize(gray_img, ((500,500)))
    max_arr = np.sum(gray_img, axis = 1)
    max_val = np.amax(max_arr, axis=0)
    breakpoints = np.zeros((1,max_arr.shape[0]), dtype = int)
    k = 0
    for i in range(0,max_arr.shape[0]):
        if i is 0:
            breakpoints[0][k] = 0
            k = k+1
            boundary_1 = -99
            boundary_2 = -99
        else:
            if max_arr[i-1] < max_val and max_arr[i] == max_val:
                boundary_1 = i
            if max_arr[i-1] == max_val and max_arr[i] < max_val:
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
        images_list.append(gray_img[breakpoints[0][i]:breakpoints[0][i+1],:])
    return images_list

def get_vertical_projection(img):
    max_arr = np.sum(img, axis = 0)
    max_val = np.amax(max_arr, axis=0)
    breakpoints = np.zeros((1,max_arr.shape[0]), dtype = int)
    k = 0
    for i in range(0,max_arr.shape[0]):
        if i is 0:
            breakpoints[0][k] = 0
            k = k+1
            boundary_1 = -99
            boundary_2 = -99
        else:
            if max_arr[i-1] < max_val and max_arr[i] == max_val:
                boundary_1 = i
            if max_arr[i-1] == max_val and max_arr[i] < max_val:
                boundary_2 = i
            if ((boundary_1 != -99) and (boundary_2 != -99) and (boundary_2 > boundary_1)):
                boundary = int((boundary_1 + boundary_2) / 2)
                breakpoints[0][k] = boundary
                boundary_1 = -99
                boundary_2 = -99
                k = k+1
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
