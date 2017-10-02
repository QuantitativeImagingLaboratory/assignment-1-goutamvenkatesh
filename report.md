RESIZE - 

1. Resample -

1a - Nearest Neighbor -

    The shape attribute was used to fetch the number of rows and columns of pixels of the particular image passed to that function.
    iterations were done on these fetched rows and columns of pixels. A color attrbute is also present in the "shape" attribute, but it 
    can be ignored if we're working with gray scale images. If the image is a colored one, we have to iterate through 3 primary colors -       Red, Green and Blue. 
    To make the method accept float values for resizing, i.e., for shrinking or zooming by a factor of 1.3, I had to change the type of       the new rows and columns to a float data type, however populating the output array had to be done with an integer data type since 
    the float type returned errors. This is why in line # 31, we have declared the two attributes, rows and columns as the integer data       type.
    
    
1b - Resizing using bilinear interpolation -

    Here, we apply the nearest neighbor technique and map the output image pixels to the appropriate input image's pixels. Using these 
    pixels that are mapped, we perform bilinear interpolation using four points and find out the intensity, or the pixel value at the
    unknown point - (i,j). This value is then assigned to the output image's pixel value at (i,j).
    
    
2. Interpolation -

2a - Linear Interpolation -

    The basic formula for linear interpolation was applied to return a point intensity using two known values.
    
2b - Bilinear Interpolation -

    Here, using four known points, we calculate one intensity of an unknown point. For this, we use linear interpolation on two known  
    points, get the intensity value of the unkown point that resides between these two known points. The same is repeated for the two
    other known points. Using the resulting values of the points that we just computed, we apply linear interpolation on these two 
    points again to get the intensity of the unknown point. 
    Change in intensity between two known points are taken and the change in intensity between a known point and the unknown point is       taken (assumed). The change in intensity between the other known point and the unknown point is taken and the arithmetic mean is         calculated.
    
    
    
