import numpy as np

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        hist = [0]*256
        
        row,col=image.shape

        for i in range(row):
            for j in range(col):
                hist[image[i, j]] += 1


        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        threshold = 0
        
        avg=len(hist)/2
        overall = 0

        for i in range(int(avg)):

            if(hist[i]!=0):
                #overall pixel intensities are added up until 'avg' length
                overall=overall+hist[i]

        overall_2 = 0
        #same thing is done for the second half
        for i in range(int(avg),int(len(hist))):

            if (hist[i] != 0):
                overall_2 = overall_2 + hist[i]

        final_threshold_1=0
        for i in range(int(avg)):
            if(hist[i]!=0):
                probability_1=hist[i]/overall
                prob_dist_1=i*probability_1
                final_threshold_1=prob_dist_1+final_threshold_1

        final_threshold_2 = 0

        for i in range(int(avg),int(len(hist))):
            if(hist[i]!=0):
                probPix=hist[i]/overall_2
                prob_dist_2=i*probPix
                final_threshold_2=prob_dist_2+final_threshold_2

        threshold=(final_threshold_1+final_threshold_2)/2

        
        return threshold

    

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()

        return bin_img


