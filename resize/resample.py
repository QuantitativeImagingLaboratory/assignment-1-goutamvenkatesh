class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here
    
        row,coloumn=image.shape
        new_row=float(row*fx)
        new_column=float(coloumn*fy)
        output_image = numpy.zeros((int(new_row),int(new_column),3), numpy.uint8)
        for i in range(int(new_row)-1):
            for j in range(int(new_column)-1):
                row_value=int(math.floor(i/fx))
                col_value=int(math.floor(j/fy))
                output_image[i,j]=image[row_value,col_value]

        
        
         return output_image


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        
        row, column = image.shape
        new_row = float(row * fx)
        new_column = float(column * fy)
        output_image = numpy.zeros((int(new_row), int(new_column), 3), numpy.uint8)

        for i in range(new_row - 1):
            x1 = math.floor(i / fx)
            x2 = math.ceil(i / fx)
            
            for j in range(new_column - 1):
                y1 = math.floor(j / fy)
                y2 = math.ceil(j / fy)

                p1 = (x1, y1, image[x1, y1])
                p2 = (x1, y1, image[x2, y1])
                p3 = (x1, y2, image[x1, y2])
                p4 = (x2, y2, image[x2, y2])
                unknown = (i, j)
               
                output_image[i, j] = bilinear_interpolation(p1, p2, p3, p4, unknown)

         return output_image

