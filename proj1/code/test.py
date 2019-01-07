import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#matplotlib inline
from utils import vis_hybrid_image, load_image, save_image
from student_code import my_imfilter, create_hybrid_image
#load_ext autoreload
#autoreload 2

image1 = load_image('../data/dog.bmp')
image2 = load_image('../data/cat.bmp')
