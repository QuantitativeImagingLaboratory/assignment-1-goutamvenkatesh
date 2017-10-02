RESIZE - 

1. Resample -

1a - Nearest Neighbor -

    The shape attribute was used to fetch the number of rows and columns of pixels of the particular image passed to that function.
    iterations were done on these fetched rows and columns of pixels. A color attrbute is also present in the "shape" attribute, but it 
    can be ignored if we're working with gray scale images. If the image is a colored one, we have to iterate through 3 primary colors -       Red, Green and Blue. 
    To make the method accept float values for resizing, i.e., for shrinking or zooming by a factor of 1.3, I had to change the type of       the new rows and columns to a float data type, however populating the output array had to be done with an integer data type since 
    the float type returned errors. This is why in line # 31, we have declared the two attributes, rows and columns as the integer data       type.
    
