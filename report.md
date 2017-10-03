RESIZE - 

1. Resample -

1a - Nearest Neighbor -

    The shape attribute was used to fetch the number of rows and columns of pixels of the particular image passed to that function.
    iterations were done on these fetched rows and columns of pixels. A color attrbute is also present in the "shape" attribute, but it 
    can be ignored if we're working with gray scale images. If the image is a colored one, we have to iterate through 3 primary colors -     Red, Green and Blue. 
    To make the method accept float values for resizing, i.e., for shrinking or zooming by a factor of 1.3, I had to change the type of 
    the new rows and columns to a float data type, however populating the output array had to be done with an integer data type since 
    the float type returned errors. This is why in line # 31, we have declared the two attributes, rows and columns as the integer data type.
    
    Here, we divide each pixel value with the resizing value and accept the floor value of it, i.e., floor(0.3) would be 0. This way, 
    each pixel in the output image is mapped to the appropriate pixel in the input image. So, if we are resizing the image by a factor 
    of 3, then fx=3; Now the first pixel of the output image - "1" would be mapped to floor(1/3), which is 0. So, the 0th pixel of the 
    input image is mapped to the 0th pixel of the output image. Now, the 2nd pixel's value would be floor(2/3), which is also 0. So, the 
    2nd pixel of the output image is also mapped to the 0th pixel of the input image, i.e., nearest neighbor.
    
    
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
    
    
    
    
    
    
3. Region Analysis-

3a. Binary Image-

-Compute Histogram -

    For each corresponding pixel value and its intensity, the "hist" list is updated with a counter. Ultimately, this results in a 2d
    array that contains the count of each kind of pixel of that particular image. This method returns a list.
    
    
-Find Optimal Threshold-
    
    First, the histogram is divided into two halves at exactly the midpoint of the graph. From here, we iterate through the first half
    of the graph and get an optimal threshold value. Simultaneously, we iterate through the second half of the graph and get another
    optimal value for that half. We keep doing this until the iterations no longer yield a better optimal solution for that particular
    half of the graph. ultimately, we get the arithmetic mean of both these final values and this is the final threshold of that graph.
    
    
    
-Binarize-

    This is a fairly simple strategy, where it involves iterating through the entire array of the image and checking if each pixel is
    above or below the attained threshold value and making that pixel value "0" or "255" based on whether it is above or below the 
    threshold value.
    

    
3b. Cell Counting -


- Blob Coloring -

    Here, we consider every possibility of the pixels in the output image. That is, we check if the pixel next to the given pixel is of
    the same intensity or not, and if it is, we don't increase the count value of that. If it is different, then we mark that pixel as a 
    different region by increasing the count value.
    The multiple "if" conditions simply make sure that we take care of every possibility of the occurence of the pixels. That is, we
    check pixels that are at the extreme left, where we can't base the count on its neighbour, since it doesn't have any, and the pixels
    for whom we have information of only the diagonal neighbour of it. Here, we compare the diagonal pixel to its adjacent pixel, and 
    if that adjacent pixel is on top of the given pixel or below it, we retain the count, hence deeming it to be under the same region.
    
   

    
