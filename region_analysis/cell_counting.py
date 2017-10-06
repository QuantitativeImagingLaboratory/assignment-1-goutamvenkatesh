import numpy
import math
import cv2

class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""

        row, col = image.shape
        count = 1
        r = numpy.zeros((row, col), numpy.uint8)
            

        for j in range(col):
            for i in range(row):
                if image[i, j] == 255:

                        if i == 0 and j > 0:
                            if r[i, j - 1] == 0:
                                r[i, j] = count
                                count = count + 1
                            if r[i, j - 1] > 0:
                                r[i, j] = r[i, j - 1]

                        if j == 0 and i > 0:
                            if r[i - 1, j] > 0:
                                r[i, j] = r[i - 1, j]
                        if r[i - 1, j] == 0:
                            r[i, j] = count
                            count = count + 1

                    
                        if i - 1 >= 0 and j - 1 >= 0:
                            if r[i, j - 1] > 0 and r[i - 1, j] == 0:
                                r[i, j] = r[i, j - 1]
                            if r[i, j - 1] == 0 and r[i - 1, j] > 0:
                                r[i, j] = r[i - 1, j]
                            if r[i, j - 1] == 0 and r[i - 1, j] == 0:
                                r[i, j] = count
                                count = count + 1

                        if r[i, j - 1] > 0 and r[i - 1, j] > 0:
                            r[i, j] = r[i, j - 1]
                            r[i - 1, j] = r[i, j - 1]
                            dec = 2
                            flag = 0
                            while flag == 0:
                                if r[i - dec, j] != 0:
                                    r[i - dec, j] = r[i - dec + 1, j]
                                    dec = dec + 1
                                else:
                                    flag = 1

        s = [0] * count
        for i in range(row):
            for j in range(col):
                if r[i, j] > 0:
                    s[r[i, j]] = s[r[i, j]] + 1

        regions = {}

        for i in range(row):
            for j in range(col):
                if r[i, j] != 0:
                    if r[i, j] in regions:
                        regions[r[i, j]].append([i, j])
                    else:
                            regions[r[i, j]] = [[i, j]]
                        

        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""



        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)
        
        stats={}
        count = 1
        for a in region.keys():

            flag=0
            for eachCoordinate in region[a]:
                if(flag==0):
                    fx=eachCoordinate[0]
                    fx2=eachCoordinate[0]
                    fy=eachCoordinate[1]
                    fy2=eachCoordinate[1]
                    flag=1
                else:
                    if(fx>eachCoordinate[0]):
                        fx=eachCoordinate[0]
                    elif(fx2<eachCoordinate[0]):
                        fx2=eachCoordinate[0]
                    if (fy > eachCoordinate[1]):
                        fy = eachCoordinate[1]
                    elif (fy2 < eachCoordinate[1]):
                        fy2 = eachCoordinate[1]

            dif1 = fx2 - fx
            avg1 = dif1 / 2
            i_count = fx + avg1
            
            dif2 = fy2 - fy
            avg2 = dif2 / 2
            j_count = fy + avg2
            
            count=count+1
            stats[count]=[len(region[a]),[i_count,j_count]]

        return 0

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        
        for a in stats.keys():
            cv2.putText(image, '*' + repr(a) + ',' + repr(stats[a][0]), (int(stats[a][1][1]), int(stats[a][1][0])), cv2.FONT_HERSHEY_SIMPLEX, 

        return image

