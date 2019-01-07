import numpy as np
import matplotlib
import matplotlib.pyplot as plt
def my_imfilter(image, filter):
  """
  Apply a filter to an image. Return the filtered image.

  Args
  - image: numpy nd-array of dim (m, n, c)
  - filter: numpy nd-array of dim (k, k)
  Returns
  - filtered_image: numpy nd-array of dim (m, n, c)

  HINTS:
  - You may not use any libraries that do the work for you. Using numpy to work
   with matrices is fine and encouraged. Using opencv or similar to do the
   filtering for you is not allowed.
  - I encourage you to try implementing this naively first, just be aware that
   it may take an absurdly long time to run. You will need to get a function
   that takes a reasonable amount of time to run so that the TAs can verify
   your code works.
  - Remember these are RGB images, accounting for the final image dimension.
  """
  
  assert filter.shape[0] % 2 == 1
  assert filter.shape[1] % 2 == 1

  ############################
  ### TODO: YOUR CODE HERE ###

  filterabs = np.abs(filter);
  filtersum = filterabs.sum();
  filter = filter/filtersum;
  [m,n,c] = image.shape;
  [k1,k2] = filter.shape;
  kmid1 = int(np.floor(k1/2));
  kmid2 = int(np.floor(k2/2));
  mpad = m + kmid1;
  npad = n + kmid2;
  fill_v = np.zeros((int(m), int(kmid2)));# (m,kimd2) array on the left 
  fill_h = np.zeros((int(kmid1),int(n+kmid2*2)));
  filtered_image =  np.zeros((m,n,c)); 
  filtered_image_paded = np.zeros((int(m+kmid1*2), int(n+kmid2*2),int(c)));
  for x in range(c):
    image_slice = image[:,:,x];
    image_slice_cx = np.hstack((fill_v,image_slice));
    image_slice_cx = np.hstack((image_slice_cx,fill_v));
    paded_image = np.vstack((image_slice_cx,fill_h)); 
    paded_image = np.vstack((fill_h,paded_image));
    paded_image_c = paded_image.copy();
    for i in range(m):#m
        for j in range(n):#n
            indx = i+kmid1;
            indy = j+kmid2;
            part = np.zeros((k1,k2));
            part = paded_image_c[indx-kmid1:indx+kmid1+1,indy-kmid2:indy+kmid2+1];
            #convol_mx = np.multiply(part,filter,casting='unsafe');
            convol_mx = np.multiply(part,filter,casting='unsafe');
            paded_image[indx,indy] = convol_mx.sum();
    filtered_image_paded[:,:,x] = paded_image;
    filtered_image[:,:,x] = np.clip(paded_image[kmid1:mpad,kmid2:n+kmid2],0,1);
    
 


    
      
  

 

  ### END OF STUDENT CODE ####
  ############################

  return filtered_image

def create_hybrid_image(image1, image2, filter):
  """
  Takes two images and creates a hybrid image. Returns the low
  frequency content of image1, the high frequency content of
  image 2, and the hybrid image.

  Args
  - image1: numpy nd-array of dim (m, n, c)
  - image2: numpy nd-array of dim (m, n, c)
  Returns
  - low_frequencies: numpy nd-array of dim (m, n, c)
  - high_frequencies: numpy nd-array of dim (m, n, c)
  - hybrid_image: numpy nd-array of dim (m, n, c)

  HINTS:
  - You will use your my_imfilter function in this function.
  - You can get just the high frequency content of an image by removing its low
    frequency content. Think about how to do this in mathematical terms.
  - Don't forget to make sure the pixel values are >= 0 and <= 1. This is known
    as 'clipping'.
  - If you want to use images with different dimensions, you should resize them
    in the notebook code.
  """

  assert image1.shape[0] == image2.shape[0]
  assert image1.shape[1] == image2.shape[1]
  assert image1.shape[2] == image2.shape[2]

  ############################
  ### TODO: YOUR CODE HERE ###
  image1_low = my_imfilter(image1, filter);
  image2_low = my_imfilter(image2, filter);
  image2_high = image2 - image2_low;
  low_frequencies = image1_low;
  high_frequencies = image2_high;
  hybrid_image = np.clip(image1_low +image2_high,0,1);
  ### END OF STUDENT CODE ####
  ############################

  return low_frequencies, high_frequencies, hybrid_image
