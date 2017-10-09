class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        #Write your code for linear interpolation here
        pt1,intensity1=pt1
        pt2,intensity2=pt2
        newPoint=unknown
        intensity_diff=pt2-pt1
        if(intensity_diff<=0):
            intensity_diff=1

        a1=pt2-newPoint
        b1=a1/intensity_diff
        x=intensity1*b1
        a2=newPoint - pt1
        b2=a2/intensity_diff
        y=intensity2*b2
        new_intensity=x+y

        return new_intensity

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May b you can reuse or call linear interpolatio method to compute this task
        
        X1,Y1, intensity1 = pt1
        X2,Y2, intensity2 = pt2
        X3,Y3, intensity3 = pt3
        X4,Y4, intensity4 = pt4
        newPointX1,newPointY1 = unknown

        newpt1=self.linear_interpolation((X1,intensity1),(X2,intensity2),newPointX1)
        newpt2=self.linear_interpolation((X3,intensity3),(X4,intensity4),newPointX1)
        newpt1=Y1,newpt1
        newpt2=Y4,newpt2
        intensity=self.linear_interpolation(newpt1,newpt2,newPointY1)
        
        

        return intensity
